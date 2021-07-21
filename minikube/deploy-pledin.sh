kubectl create deployment pagweb --image=josedom24/aplicacionweb:v1
kubectl expose deployment pagweb --port=80 --type=NodePort
kubectl get svc
kubectl get po -o wide
kubectl get po -o wide
wget https://raw.githubusercontent.com/ahmetb/kubectx/master/kubens
