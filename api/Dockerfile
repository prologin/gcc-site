FROM ubuntu:21.04
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y python3-venv python3-pip && \
    mkdir /srv/api

WORKDIR /srv/api
ADD requirements.txt /srv/api
RUN python3 -m venv venv && \
    . ./venv/bin/activate && \
    pip3 install -r requirements.txt

ADD gccsite /srv/api/gccsite
ADD ./entrypoint-dev.sh .
ENTRYPOINT [ "/srv/api/entrypoint-dev.sh" ]
