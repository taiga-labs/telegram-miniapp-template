FROM nginx:latest

WORKDIR /etc/nginx/ssl
COPY nginx/certs/selfsign.sh .
RUN chmod +x ./selfsign.sh
RUN ./selfsign.sh
RUN chmod 444 nginx-selfsigned.key
RUN chmod 444 nginx-selfsigned.crt

WORKDIR /etc/nginx
COPY nginx/conf/443.conf ./nginx.conf

ENTRYPOINT ["nginx", "-g", "daemon off;"]
