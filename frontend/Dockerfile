FROM node:20

WORKDIR /usr/src/super-pancake

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]
