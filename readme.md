# Embryo Image Generated or Real

## [Paper](https://www.nature.com/articles/s41598-025-94680-0) | [GitHub](https://github.com/orianapresacan/Embryo) | [GitHub GeneratedOrReal](https://github.com/AlexDorobantiu/GeneratedOrReal)

## Overview

This repository contains code for the web application that allows users to give predictions and feedback on whether the image is generated or real.


## How to run the application

Copy all the generated and real images in the "images" folder!

## To build from scratch

You must have nodejs installed. It can be downloaded from https://nodejs.org/en/download/

You must have Docker desktop installed. It can be downloaded from https://www.docker.com/products/docker-desktop

From the "front" folder, run the following commands:

```npm install```

```npm run build```


## How to run with docker

First build the image by running this command in the root folder:

```docker build -t gor:v1 .```

Run the image with the following command, replacing the `results_on_host`` folder with a valid path on your machine:
 
```docker run -d --mount type=bind,source=/results_on_host,target=/results -p 80:80 gor:v1```


After that, you can access the application on http://localhost/9e0a8953-92d7-428e-97f5-e94f8ef5fef2/login.html

## How to download the responses

The responses should be available in the folder you specified in the previous step.

## Hot to convert the mask responses

The `results` folder has a python script `convert_markings.py` which converts the mask results from its current folder into the `.png` image format.

To run the script:
```bash
python convert_markings.py
```

The script needs the `pillow` and `numpy` libraries, so make sure you have those installed.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Citation:
```
Presacan, O., Dorobanţiu, A., Thambawita, V. et al. Merging synthetic and real embryo data for advanced AI predictions. Sci Rep 15, 9805 (2025). https://doi.org/10.1038/s41598-025-94680-0
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## For more details:
Please contact: alexandru.dorobantiu@ulbsibiu.ro