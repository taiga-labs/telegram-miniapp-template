FROM nginx:latest

RUN rm -rf /usr/share/nginx/html/*
COPY ./src/ /usr/share/nginx/html

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT ["nginx", "-g", "daemon off;"]