### Copy all the generated and real images in the "images" folder!

## To build from scratch

You must have nodejs installed. It can be downloaded from https://nodejs.org/en/download/

You must have Docker desktop installed. It can be downloaded from https://www.docker.com/products/docker-desktop

From the "front" folder, run the following commands:

```npm install```

```npm run build```


## How to run with docker

First build the image by running this command in the root folder:

```docker build -t gor:v1 .```

Run the image with the following command:
 
```docker run -d -p 80:80 gor:v1```


After that, you can access the application on http://localhost/static/login.html

## How to download the responses

Open the Docker desktop application

Click on the gor container

Click on the Files tab

Navigate to the "code" folder

Download the .json files named after the users