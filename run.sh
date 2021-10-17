#!/bin/bash

source .env

get_health() {
	docker inspect --format '{{.State.Health.Status}}' $1
}

if [ $CREATE_CONTAINER -ne 0 ]
then
	case $RDBMS in
		'postgres')
			DOCKER_PORT=5432
			PREFIX='POSTGRES'
			;;
		'mysql')
			DOCKER_PORT=3306
			PREFIX='MYSQL'
			;;
		*)
			echo "Unsupported RDBMS: $RDBMS"
			return 2
			;;
	esac
	docker container stop $CONTAINER_NAME && docker container rm $CONTAINER_NAME
	docker build -t $IMAGE_NAME $RDBMS
	docker run -d -p $PORT:$DOCKER_PORT --name $CONTAINER_NAME \
		-e ${PREFIX}_USER=$USER -e ${PREFIX}_PASSWORD=$PASSWORD \
		-e ${PREFIX}_DB=$DB -e ${PREFIX}_DATABASE=$DB \
		-e MYSQL_ROOT_PASSWORD=$PASSWORD $IMAGE_NAME

	
	while [ $(get_health $CONTAINER_NAME) != 'healthy' ]
	do
		sleep 1
	done
fi

source venv/bin/activate
python src/generate_data.py