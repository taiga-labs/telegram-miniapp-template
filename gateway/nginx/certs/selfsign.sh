openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./nginx-selfsigned.key -out ./nginx-selfsigned.crt -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.com"
