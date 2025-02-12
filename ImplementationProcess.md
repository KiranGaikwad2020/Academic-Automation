# Following are the steps used to create dockerized application
1. Developed Python Application **(performancecategory_app.py)**
2. Created **requirements.txt** file
3. Developed **Dockerfile** to convert application into dockerized application.
4. Built the docker image of application using following command-
   **$ docker build -t student-classification-app .**
5.  Run the Docker Container
   **$ docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd)/output:/app/output student-classification-app**
   Where,
   **-e DISPLAY=$DISPLAY**: Allows GUI display on host machine.
   **-v /tmp/.X11-unix:/tmp/.X11-unix**: Enables X11 forwarding (Linux GUI support).
   **-v $(pwd)/output:/app/output**: Mounts an output directory so files are accessible on the host.
