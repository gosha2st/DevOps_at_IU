# [F21] DevOps core course at Innopolis University
> Author: Georgii Stepanov, B18-SB  
g[dot]stepanov[at]innopolis.university

This repository contains my **lab submissions** for the *[F21] DevOps* core course at *Innopolis University*.

## Overview
This is simplest Python web application, written using *Flask* and *pytz* frameworks, that shows current time in the specified timezone, which is Moscow (UTC+03:00) by default.

It also tracks the history of visits of the root path along with their time, and can display it at the `/visits` url.

## Installation and Getting started
1. Firstly make sure you have [Python 3.9+](https://python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed on your machine.
2. Download this repository to your local storage:  
`git clone http://github.com/gosha2st/IU_DevOps`
3. Create virtual environment:  
    ```
    python -m virtualenv venv 
    source venv/bin/activate
    ```
4. Make sure you have required packages installed:  
`pip install -r requirements.txt`
5. Run the Python Flask web app:  
`python app.py`

The app showing current Moscow time is now available on your localhost at port `5000`:  
`http://127.0.0.1:5000/`

![](https://i.imgur.com/xsTR5D7.png)


You can also access the visits of the root path history along with their time at:  
`http://127.0.0.1:5000/visits/`

![](https://i.imgur.com/JioQe42.png)


## Unit testing
*PyTest* was used as a framework for automated *Unit testing*.

To run pre-defined simple Unit tests suite:  
`pytest`  
in the project's folder.

![](https://i.imgur.com/NOE56Sb.png)


To see and edit tests, refer to the `test_app.py` file in the `tests` folder.


## Docker

### Building Image locally
1. Firstly, make sure that Docker Desktop is installed on your machine.  
For this, run the following command in the terminal / command line:  
`docker -v`  
In case Docker Desktop is not installed, download it from:  
http://docs.docker.com/engine/install/
2. Secondly, make sure you've downloaded project repository to your local storage:  
`git clone http://github.com/gosha2st/IU_DevOps`
3. Enter the app folder:  
`cd app_python`
4. Build the image:  
`(sudo) docker build -t gosha2st/app_python .`  
![](https://i.imgur.com/9OZIb8G.png)
5. Run the container.  
`docker run --rm -it -p 5000:5000 gosha2st/app_python`  
Simple web app showing current Moscow time is now available at:  
http://localhost:5000/  
![](https://i.imgur.com/ByEEV9v.png)

### Fetching pre-built image from Docker Hub
1. Check the existing image on Docker Hub:  
http://hub.docker.com/r/gosha2st/devops-app_python  
![](https://i.imgur.com/4Ytsr7U.png)
2. Fetch the image to your local storage:  
`docker pull gosha2st/devops-app_python:ap_first`
3. Run the container.  
`docker run --rm -it -p 5000:5000 gosha2st/app_python`  
Simple web app showing current Moscow time is now available at:  
http://localhost:5000/  


## License
This project is licensed under the **MIT** License:  
http://mit-license.org/  
http://github.com/gosha2st/IU_DevOps/blob/main/LICENSE
