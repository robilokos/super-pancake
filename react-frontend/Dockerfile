FROM node:20

WORKDIR /usr/src/super-pancake/react-frontend

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "dev"]
