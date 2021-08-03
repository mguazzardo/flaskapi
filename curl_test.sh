IP=$(docker inspect flaskapi | grep -i IPA | grep 172 | tail -1 | awk -F: '{print $2}' | awk -F\" '{print $2}')

if curl $IP:5000/ping
then
	echo "URL andando correctamente"
else
	echo "El contenedor no funciona"
	exit 1
fi
