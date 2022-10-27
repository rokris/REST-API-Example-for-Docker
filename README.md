# REST-API Example in a container
# Python / Flask

## Build Configuration/Management
We'll create a file called "Dockerfile" that contains the steps and information needed to build an image.

The build process is done in layers, with the starting point typically being an operating system or, more likely, an OS and framework combination. For example, you need Python 3 installed. So it's pretty common to start from that point. You can -- and there might be good reasons for this -- start with the operating system and then install the framework all inside your image as you build it. You can also do just that -- start with an OS and add a framework -- and save that image and use it as your base for other images.

Yes, like any IT technology, you can make this as simple or as complicated as you like. We'll start with an OS+Framework combination to keep things simple. We'll then copy our code in the image, then make sure the dependencies are installed. Then, we'll give the image a command to be executed when someone runs the image in a container. The following file, "Dockerfile" does those things:

```Dockerfile
FROM python:3
ADD rest-example.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 8080
CMD [ "python", "./rest-example.py"]
```

A line-by-line explanation is later in this article, but let's just build thing and run it; we can come back to the details.
#
## Let's Get Some Code
Fork or clone the github repository at

https://github.com/rokris/REST-API-Example-for-Docker

Move into the directory
#
## Let's Build And Run

### To build the image, run

```bash
docker build -t rest-example .
```

### To run the image (again, we'll dive into this later), run
```bash
docker run -p 8080:8080 rest-example
```

### Finally, open a second terminal window and run
```bash
curl http://localhost:8080
```

### You should see the web page as the result.
#
## The Cycle
So that's the basic cycle:

    Create the source code
    Create a Dockerfile file
    Build the image
    Run the image in a container


## About that Dockerfile
The file “Dockerfile” is used to guide the construction of your image. Here’s a short, step-by-step breakdown:

```Dockerfile
FROM python:3
```

This is your base image, the starting point. In this case, it’s the official image from the Python Software Foundation and has Python:3 installed. That means we don’t have to install any framework; it’s already included with this base image. 
#
```Dockerfile
ADD rest-example.py /
```
Copies the program into the image.
#
```Dockerfile
RUN pip install flask
RUN pip install flask_restful
```
Install the packages necessary for our code into the image.
#
```Dockerfile
EXPOSE 8080
```
Exposes the application port, 8080, to the outside world.
#
```Dockerfile
CMD [ "python", "./rest-example.py"]
```

This is what runs when the image is started (i.e. docker run).
# 
## Running In A Container
Running the ```docker run -p 8080:8080 rest-example``` command starts the image in a container. It code uses port 8080, and it is mapped to the local port 8080. Feel free to experiment with this. It will be attached to your command line; that is, it ties up your terminal while it’s running. You can eliminate this by using the --detach option in your command. In that case, the container runs in the background.

You can see the results of the code by running the curl command or opening your browser to http://localhost:8080.
#
## Test PUT
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Shovon", "balance": 100}' http://127.0.0.1:8080/account
```
## Lets publish to the Docker Hub

```bash
docker login
docker tag rest-example <dockerhubusername>/rest-example:v1
docker push <dockerhubusername>/rest-example:v1
```
