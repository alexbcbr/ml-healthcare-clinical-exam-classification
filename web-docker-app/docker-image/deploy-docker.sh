docker build -t w:beta . 
docker run --name web -p 8080:80 -it w:beta /bin/bash