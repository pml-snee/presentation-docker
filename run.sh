 docker rm my-first-container;

 docker run \
		-p 80:8080 \
 --name my-first-container \
 --mount type=bind,source="$(pwd)"/storage,target=/external \
 example-app 

