FROM python:latest
LABEL authors="LiuZhongLiang"
RUN mkdir /home/work
WORKDIR /home/work
RUN cd /home/work
COPY . .
RUN apt-get upgrade
RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x bin/install.sh
RUN bin/install.sh