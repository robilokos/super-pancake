# super-pancake
- run the application:
    - clone repository
    - download docker to your desktop
    - run `docker-compose up` command in the root folder
    - go to `http://localhost:8080/` to reach the app

- how to reproducate the application:
    - frontend:
        - install node to your computer
        - go to the root folder
        - run `npm install -g @vue/cli` for installing the vue cli
        - run `vue create frontend` to create the vue.js project
        - go to the frontend folder: `cd frontend/`
        - install additional dependencies:
            - `vue add typescript` - for using ts in the project, static typing
            - `vue add vuex` - for state management
            - `npm install axios` - for api calls
        - create the Dockerfile in the frontend folder
    
    - backend:
        - go to the root folder, create the backend folder and go into that `mkdir backend`, `cd backend`
        - create the main.py file and configure the fastapi app, db connection, cors, etc..
        - create the requirements.txt
        - create the Dockerfile in the backend folder

    - create the docker-compose.yml file with the services