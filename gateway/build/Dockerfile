FROM nginx:latest

COPY ./nginx/certs/nginx-selfsigned.crt /etc/nginx/ssl/nginx-selfsigned.crt
COPY ./nginx/certs/nginx-selfsigned.key /etc/nginx/ssl/nginx-selfsigned.key
RUN chmod 444 /etc/nginx/ssl/nginx-selfsigned.crt
RUN chmod 444 /etc/nginx/ssl/nginx-selfsigned.key

COPY ./nginx/conf/443.conf /etc/nginx/nginx.conf

ENTRYPOINT ["nginx", "-g", "daemon off;"]
