docker build -t w:beta4 .
docker tag w:beta4 771620814942.dkr.ecr.us-east-1.amazonaws.com/webdoctor:latest

kubectl apply -k ./
kubectl get pods
kubectl get service