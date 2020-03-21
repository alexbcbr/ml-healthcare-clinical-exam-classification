# Indicar a imagem base
FROM ubuntu

LABEL Alex BC

ENV VARIABLE1=development
ENV PORT=80

#append no arquivo para inicializar o apache de forma automatica
RUN echo "test" >> /test.txt
RUN apt-get update && apt-get install -y apache2 curl
RUN echo "service apache2 start" >> /etc/bash.bashrc 

# Criar um arquivo
COPY ./web/medical/dist /var/www/html
WORKDIR /var/www
#VOLUME ["/var/www"]

EXPOSE $PORT

#ENTRYPOINT ["node", "server.js"]
