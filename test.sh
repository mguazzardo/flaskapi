SALIDA=$(docker ps | grep flaskapi | grep -v k8s)
if [ ! -z "$SALIDA" ]
then
              echo "esta corriendo una imagen"
              exit 1
else
              echo "No hay imagen corriendo"
fi 
