SALIDA=$(docker ps | grep flaskapi | grep -v k8s)
if [ ! -z "$SALIDA" ]
then
              echo "esta corriendo una imagen"
              exit 0
else
              docker run -d --name=flaskapi -p 5000:5000 mguazzardo/curso-jenkins:$BUILD_NUMBER
fi 
