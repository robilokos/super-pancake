# super-pancake
- run the application:
    - clone repository
    - download docker to your desktop
    - run `docker-compose up --build` command in the root folder
    - go to `http://localhost:8080/` to reach the app

- how to reproducate the application:
    - frontend:
        - install node to your computer
        - go to the root folder
        - run `npm create vite@latest`
            - add the name of the project, e.g: `react-frontend`
            - choose `React` then `typescript`
        - go to the frontend folder: `cd react-frontend/`
        - install additional dependencies:
            - `npm install bootstrap@latest` - for Bootstrap styles
            - `npm install axios` - for API calls
            - `npm install @mui/icons-material @mui/material @emotion/styled @emotion/react` - for Material UI
        - add `import 'bootstrap/dist/css/bootstrap.css'` into the `main.tsx` file
        - add `server: {host: true, strictPort: true, port: 8080}` into the `vite.config.ts` file, under `plugins`
        - create the Dockerfile in the react-frontend folder
    
    - backend:
        - go to the root folder, create the backend folder and go into that `mkdir backend`, `cd backend`
        - create the main.py file and configure the fastapi app, db connection, cors, etc..
        - create the requirements.txt
        - create the Dockerfile in the backend folder

    - create the docker-compose.yml file with the services

- docker-compose.yml

```
version: '3'

services:
  react-frontend:
    build: <project_path>/super-pancake/react-frontend
    ports:
      - "8080:8080"
    restart: always
    depends_on:
      - backend
    volumes:
      - <project_path>/super-pancake/react-frontend:/usr/src/super-pancake/react-frontend
      - /usr/src/super-pancake/react-frontend/node_modules

  backend:
    build: <project_path>/super-pancake/backend
    ports:
      - "8000:8000"
    restart: always
    depends_on:
      - mongodb
      - mysqldb
    environment:
      MONGO_URI: "mongodb://mongodb:27017/<database_name>"
      MYSQL_HOST: "mysql"
      MYSQL_PORT: "3306"
    volumes:
      - <project_path>/super-pancake/backend:/usr/src/super-pancake/backend

  mongodb:
    image: "mongo"
    ports:
      - "27017:27017"
    restart: always

  mysqldb:
    image: "mysql:latest"
    command: --default-authentication-plugin=mysql_native_password
    ports:
      - "3306:3306"
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: "admin"
      MYSQL_DATABASE: "<database_name>"
      MYSQL_USER: "<user_name>"
      MYSQL_PASSWORD: "<password>"
```