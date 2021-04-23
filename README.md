# docker-neuroportdbs-build
Build the docker image for NeuroportDBS. 

#### 1. Download the Repository

    $ git clone https://github.com/dave6892/docker-neuroportdbs-build.git
    $ cd docker-neuroportdbs-build
    
#### 2. Move the Data to the Repository   
Move the data (\*.ns5 and associated files) into the direcory `./data`.

#### 3. Pull the Docker Image and Compose
    $ docker-compose up -d --build
    
#### 4. Configure the Environment and Run in Docker
    $ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}') xhost +
    $ docker-compose run --rm -e DISPLAY=$IP:0 app


### Inside the Docker CLI
#### For the first time running this application, make sure to run
    $ serf-makemigrations; serf-migrate

#### Import Data into the Database
    $ python import_ns5.py
    
#### Run GUI
    $ python features_gui.py
