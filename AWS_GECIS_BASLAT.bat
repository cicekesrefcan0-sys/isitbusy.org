@echo off
echo ========================================
echo    AWS GECIS SURECI BASLANGICI
echo ========================================
echo.

echo [1/5] Mevcut sistem backup aliniyor...
echo.

REM MongoDB backup
echo MongoDB backup aliniyor...
if exist backup mkdir backup
mongodump --host localhost:27017 --db isitbusy --out ./backup/mongodb_backup_%date:~-4,4%%date:~-10,2%%date:~-7,2%
if %errorlevel% equ 0 (
    echo ✅ MongoDB backup basarili
) else (
    echo ❌ MongoDB backup hatasi - MongoDB calismiyor olabilir
)

REM Environment backup
echo.
echo Environment dosyalari yedekleniyor...
copy esref1-main\backend\.env esref1-main\backend\.env.backup >nul 2>&1
copy esref1-main\frontend\.env esref1-main\frontend\.env.backup >nul 2>&1
copy .env .env.backup >nul 2>&1
echo ✅ Environment dosyalari yedeklendi

echo.
echo [2/5] AWS CLI kontrol ediliyor...
aws --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ AWS CLI kurulu
) else (
    echo ❌ AWS CLI kurulu degil
    echo AWS CLI indiriliyor...
    curl "https://awscli.amazonaws.com/AWSCLIV2.msi" -o "AWSCLIV2.msi"
    echo AWSCLIV2.msi dosyasi indirildi - Manuel kurulum gerekli
    pause
)

echo.
echo [3/5] Python bagimliliklar kontrol ediliyor...
pip show boto3 >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ boto3 kurulu
) else (
    echo boto3 kuruluyor...
    pip install boto3
)

echo.
echo [4/5] AWS Bedrock test dosyasi olusturuluyor...
(
echo import boto3
echo import json
echo import sys
echo.
echo def test_bedrock_connection^(^):
echo     """AWS Bedrock baglantisini test et"""
echo     try:
echo         client = boto3.client^('bedrock-runtime', region_name='us-east-1'^)
echo         
echo         # Basit bir test prompt'u
echo         prompt = "Hello, can you respond with 'AWS Bedrock is working'?"
echo         
echo         body = json.dumps^({
echo             "anthropic_version": "bedrock-2023-05-31",
echo             "max_tokens": 50,
echo             "messages": [
echo                 {
echo                     "role": "user",
echo                     "content": prompt
echo                 }
echo             ]
echo         }^)
echo         
echo         response = client.invoke_model^(
echo             modelId='anthropic.claude-3-sonnet-20240229-v1:0',
echo             body=body,
echo             contentType='application/json'
echo         ^)
echo         
echo         result = json.loads^(response['body'].read^(^)^)
echo         print^("✅ AWS Bedrock Test Basarili!"^)
echo         print^("Response:", result['content'][0]['text']^)
echo         return True
echo         
echo     except Exception as e:
echo         print^("❌ AWS Bedrock Test Hatasi:", str^(e^)^)
echo         print^("Olasi nedenler:"^)
echo         print^("1. AWS credentials yapılandırılmamış ^(aws configure^)"^)
echo         print^("2. Bedrock model access istenmemiş"^)
echo         print^("3. Internet baglantisi sorunu"^)
echo         return False
echo.
echo if __name__ == "__main__":
echo     test_bedrock_connection^(^)
) > test_bedrock.py

echo ✅ test_bedrock.py olusturuldu

echo.
echo [5/5] AWS Bedrock AI servisi olusturuluyor...
if not exist esref1-main\backend\services\aws_bedrock_service.py (
(
echo """
echo AWS Bedrock AI Service - Google Gemini alternatifi
echo """
echo import boto3
echo import json
echo import logging
echo from typing import Optional, Dict
echo from datetime import datetime
echo.
echo logger = logging.getLogger^(__name__^)
echo.
echo class AWSBedrockService:
echo     """AWS Bedrock AI Service"""
echo     
echo     def __init__^(self^):
echo         try:
echo             self.client = boto3.client^('bedrock-runtime', region_name='us-east-1'^)
echo             self.model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
echo             logger.info^("AWS Bedrock initialized successfully"^)
echo         except Exception as e:
echo             logger.error^(f"AWS Bedrock initialization failed: {e}"^)
echo             self.client = None
echo     
echo     async def predict_busyness^(self, venue_data: dict^) -> dict:
echo         """AWS Bedrock ile mekan yogunlugu tahmini"""
echo         if not self.client:
echo             return {"error": "AWS Bedrock not initialized"}
echo         
echo         try:
echo             venue_name = venue_data.get^('name', 'Unknown'^)
echo             venue_type = venue_data.get^('type', 'Unknown'^)
echo             current_time = venue_data.get^('current_time', datetime.now^(^).strftime^('%Y-%m-%d %H:%M'^)^)
echo             
echo             prompt = f"""
echo             Venue Analysis Request:
echo             - Name: {venue_name}
echo             - Type: {venue_type}  
echo             - Current Time: {current_time}
echo             
echo             Please predict the busyness level ^(1-5 scale^) and provide reasoning.
echo             Format your response as:
echo             Busyness Level: X/5
echo             Reasoning: ^[your explanation^]
echo             """
echo             
echo             body = json.dumps^({
echo                 "anthropic_version": "bedrock-2023-05-31",
echo                 "max_tokens": 300,
echo                 "messages": [{"role": "user", "content": prompt}]
echo             }^)
echo             
echo             response = self.client.invoke_model^(
echo                 modelId=self.model_id,
echo                 body=body,
echo                 contentType='application/json'
echo             ^)
echo             
echo             result = json.loads^(response['body'].read^(^)^)
echo             ai_response = result['content'][0]['text']
echo             
echo             return {
echo                 "success": True,
echo                 "prediction": ai_response,
echo                 "source": "aws_bedrock",
echo                 "model": "claude-3-sonnet",
echo                 "timestamp": datetime.now^(^).isoformat^(^)
echo             }
echo             
echo         except Exception as e:
echo             logger.error^(f"Bedrock prediction error: {e}"^)
echo             return {
echo                 "success": False,
echo                 "error": str^(e^),
echo                 "fallback": "Unable to predict busyness - AWS Bedrock error"
echo             }
echo     
echo     async def chat_with_ai^(self, message: str, context: dict = None^) -> dict:
echo         """AWS Bedrock ile chat"""
echo         if not self.client:
echo             return {"error": "AWS Bedrock not initialized"}
echo         
echo         try:
echo             prompt = f"User message: {message}"
echo             if context:
echo                 prompt += f"\nContext: {json.dumps^(context^)}"
echo             
echo             body = json.dumps^({
echo                 "anthropic_version": "bedrock-2023-05-31", 
echo                 "max_tokens": 500,
echo                 "messages": [{"role": "user", "content": prompt}]
echo             }^)
echo             
echo             response = self.client.invoke_model^(
echo                 modelId=self.model_id,
echo                 body=body,
echo                 contentType='application/json'
echo             ^)
echo             
echo             result = json.loads^(response['body'].read^(^)^)
echo             ai_response = result['content'][0]['text']
echo             
echo             return {
echo                 "success": True,
echo                 "response": ai_response,
echo                 "source": "aws_bedrock"
echo             }
echo             
echo         except Exception as e:
echo             logger.error^(f"Bedrock chat error: {e}"^)
echo             return {
echo                 "success": False,
echo                 "error": str^(e^)
echo             }
echo.
echo # Global instance
echo bedrock_service = AWSBedrockService^(^)
) > esref1-main\backend\services\aws_bedrock_service.py

echo ✅ AWS Bedrock servisi olusturuldu
) else (
echo ✅ AWS Bedrock servisi zaten mevcut
)

echo.
echo ========================================
echo           GECIS HAZIRLIK TAMAMLANDI
echo ========================================
echo.
echo Sonraki adimlar:
echo.
echo 1. AWS hesabi acin: https://aws.amazon.com/free/
echo 2. AWS CLI yapilandirin: aws configure
echo 3. Bedrock model access isteyin ^(AWS Console^)
echo 4. Test calistirin: python test_bedrock.py
echo.
echo Detayli rehber: AWS_BASLANGIC_ADIMLAR.md
echo Tam plan: AWS_GECIS_PLANI.md
echo.
pause