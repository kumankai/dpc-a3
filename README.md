Commands to run images:
1. docker-compose build
2. docker-compose run --rm client

This runs all of the images, except the client container is dettached from the composition with interactive mode on.

When client is exited, the rest of the container will still be running.

Command to stop containers:
docker-compose down