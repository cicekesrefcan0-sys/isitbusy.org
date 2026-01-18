module.exports = {
  apps: [{
    name: 'isitbusy-backend',
    script: 'real_data_backend.py',
    interpreter: 'py',
    cwd: './backend',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    restart_delay: 5000,
    max_restarts: 10,
    min_uptime: '10s',
    env: {
      NODE_ENV: 'production',
      PORT: 8003,
      PYTHONPATH: './backend',
      REACT_APP_BACKEND_URL: 'http://localhost:8003'
    },
    env_development: {
      NODE_ENV: 'development',
      PORT: 8003,
      PYTHONPATH: './backend'
    },
    error_file: './logs/backend-error.log',
    out_file: './logs/backend-out.log',
    log_file: './logs/backend-combined.log',
    time: true,
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
    merge_logs: true,
    log_type: 'json'
  }, {
    name: 'isitbusy-frontend',
    script: 'npm',
    args: 'start',
    cwd: './frontend',
    instances: 1,
    autorestart: true,
    watch: false,
    env: {
      NODE_ENV: 'production',
      PORT: 3000,
      REACT_APP_BACKEND_URL: 'http://localhost:8003'
    },
    env_development: {
      NODE_ENV: 'development',
      PORT: 3000,
      REACT_APP_BACKEND_URL: 'http://localhost:8003'
    },
    error_file: './logs/frontend-error.log',
    out_file: './logs/frontend-out.log',
    log_file: './logs/frontend-combined.log',
    time: true
  }]
};