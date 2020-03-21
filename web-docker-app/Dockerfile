# Indicar a imagem base
FROM nginx

LABEL Alex BC

ENV VARIABLE1=development
ENV PORT=80

#append no arquivo para inicializar o apache de forma automatica
#RUN echo "test" >> /test.txt
RUN apt-get update && apt-get install -y curl
RUN echo "service nginx start" >> /etc/bash.bashrc 

# Criar um arquivo
COPY ./web/medical/dist /usr/share/nginx/html
WORKDIR /usr/share/nginx/html
#VOLUME ["/var/www"]

EXPOSE $PORT

#ENTRYPOINT ["node", "server.js"]
