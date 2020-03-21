kubectl delete deployment webdoctor
kubectl delete service webdoctor

docker rmi 771620814942.dkr.ecr.us-east-1.amazonaws.com/webdoctor:latest
docker rmi w:beta4