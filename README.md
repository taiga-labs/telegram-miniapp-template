# telegram-miniapp-template

## About
Fullstack Telegram WebApp (aiogram 3 + fastapi + socketio + Vanilla JS)  
Run Docker compose to test WebApp with self-signed certs on your local machine

## Quickstart
1. create template database
  ```sh
  sudo -u postgres psql -c 'create database template;'
  ```
2. run alembic migration
  ```sh
  sudo python alembic_tool.py
  ```
3. set required env variables  
   ```APP_CONFIG__DB__URL``` - database url  
   ```APP_CONFIG__BOT__TOKEN``` - your bot token  
   ```APP_CONFIG__MAPP__HOST``` - webapp access address (docker interface ip for local use)  

4. run docker compose
  ```sh
  sudo docker compose up --build -d
  ```

## Organization
![Alt text](images/1.jpg?raw=true "Schema")
### Backend
1. **bot** - simple aiogram bot template + user id database storage 
2. **webapp** - fastapi + socketio backend 
### Frontend
  Static JS view
### Gateway
  Nginx proxy with self signed certs for accessing WebApp bypassing Telegram HTTP protocol ban  
  Also can be used as a proxy for telegram webhooks
