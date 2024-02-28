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