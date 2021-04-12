FROM dave6892/serf:latest
ENV DEBIAN_FRONTEND=noninteractive
ENV GITHUB_TOKEN=f455644c7845ce323a0a128fdb21900653f8c3fd

# Add user
RUN adduser --quiet --disabled-password qtuser && usermod -a -G audio qtuser
RUN mkdir /tmp/runtime-qtuser && chown 1000 /tmp/runtime-qtuser
WORKDIR /app

# Install dependencies
RUN apt-get update \
&& apt-get install -y git \
python3-dev \
python3-pip \
python-is-python3 \
build-essential \
default-libmysqlclient-dev \ 
cmake \
qt5-default 

# Install CereLink
RUN pip3 install Cython numpy \
&& git clone https://github.com/dashesy/CereLink.git \
&& cd /app/CereLink && rm -Rf build dist \
&& mkdir build && cd /app/CereLink/build \
&& cmake .. && cmake --build . --config Release \
&& cd /app/CereLink \
&& python3 setup.py install

# Install NeuroportDBS
RUN pip3 install pyserial \
numpy \
scipy \
# pyaudio \
PyFFTW \
pylsl \
quantities \
regex \
pyqt5 \
qtpy \
pyqtgraph \
git+https://github.com/NeuralEnsemble/python-neo.git \
git+https://github.com/SachsLab/pytf.git \
git+https://github.com/SachsLab/mspacman.git \
git+https://github.com/SachsLab/cerebuswrapper.git \
git+https://${GITHUB_TOKEN}@github.com/SachsLab/NeuroportDBS.git

#Set working directory
WORKDIR /app
ADD my_serf.cnf /home/qtuser