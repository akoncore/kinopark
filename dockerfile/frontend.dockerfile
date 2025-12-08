FROM node:18-alpine as build-stage

WORKDIR /kinopart-frontend

COPY package*.json ./

RUN npm install
COPY . .

RUN npm run build

FROM nginx:stable-alpine as production-
    
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build-stage /kinopart-frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD [ "nginx","-g","daemon off" ]