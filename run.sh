 docker rm my-first-container;

 docker run \
 -p 80:8080 \
 -it \
 --name my-first-container \
 --mount type=bind,source="$(pwd)"/storage,target=/external \
 --mount type=bind,source="$(pwd)"/test,target=/test \
 example-app /bin/bash \
