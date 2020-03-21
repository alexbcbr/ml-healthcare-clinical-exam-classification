kubectl get namespace

kubectl get nodes
kubectl get nodes -o=wide

kubectl get pods                        #list pods running in the default namespace
kubectl get pods -w
kubectl get pods --all-namespaces
kubectl get pod --namespace=kube-system
kubectl describe pods

kubectl logs <pod-name>

kubectl create deployment --image nginxdemos/hello web1
kubectl get deployments
kubectl scale deployment web1 --replicas=5

kubectl expose deployment web1 --port=80 --type=LoadBalancer
kubectl get service

kubectl get pv          #get persistent volumes
kubectl get pvc          #get persistent volumes claims

kubectl set image deploy/wordpress wordpress=wp5
kubectl rollout undo deploy/wordpress
kubectl rollout history deploy
kubectl rollout status deploy/wordpress

k config set-context --current --namespace=kube-system  ##change namespace
k config view | grep namespace  ##check to see your namespace

kubectl delete deployments web1
kubectl delete services web1

k exec -it frontend-58b4574cd9-cmq79 /bin/bash
k exec frontend-58b4574cd9-cmq79 -- ls -al

k edit pod frontend-58b4574cd9-cmq79

##### GUI Console (https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
k apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta6/aio/deploy/recommended.yaml
url: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

###### Sample applications
https://github.com/nigelpoulton/k8s-sample-apps
