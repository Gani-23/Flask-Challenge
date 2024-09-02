To build a Docker image, follow these steps:

1. Create a Dockerfile in the root directory of your project. This file will contain instructions for building the image.

2. Start the Docker build process by running the following command in your terminal:
    ```
    docker build -t <image_name> .
    ```

    Replace `<image_name>` with the desired name for your image.

3. Docker will read the Dockerfile and execute the instructions to build the image. This may include installing dependencies, copying files, and configuring the environment.

4. Once the build process is complete, you can verify that the image was created by running:
    ```
    docker images
    ```

    This command will display a list of all the Docker images on your system.

5. To run a container using the newly built image, use the following command:
    ```
    docker run -d -p <host_port>:<container_port> <image_name>
    ```

    Replace `<host_port>` and `<container_port>` with the desired port numbers for the host and container, respectively.

That's it! You have successfully built a Docker image and run a container based on it. You can now distribute and deploy your application using Docker.