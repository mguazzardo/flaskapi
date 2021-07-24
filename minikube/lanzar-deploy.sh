kubectl create deployment pagweb --image=josedom24/aplicacionweb:v1
kubectl expose deployment pagweb --port=80 --type=NodePort
