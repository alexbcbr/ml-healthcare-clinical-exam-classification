docker build -t w:beta3 . 
#kubectl run webmedical --image=w:beta
kubectl create deployment --image w:beta2 webdoctor
kubectl expose deployment webdoctor --port=80 --type=LoadBalancer
