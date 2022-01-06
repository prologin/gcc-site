# GCC site

# Contributing
## Local Dev with front

### Installing dependencies
Dependencies needed
- git
- yarn
For the docker-compose setup for the backend you need
- docker
- docker-compose

#### To install git / yarn

To install git / yarn you only need :
```
apt-get update && apt-get install -y git yarn
```
on Debian / Ubuntu and their derivatives.

#### Install Docker

See `https://docs.docker.com/engine/install/ubuntu/` :).

#### Install Docker-Compose

See `https://docs.docker.com/compose/install/` :)
Select `Linux` and proceed with installation.

/!\ Be careful NOT TO use `pip` to install docker-compose system-wise.
This is almost certain to break your system.

#### Local setup

Go into ./test and launch `sudo docker-compose up -d` [1].
It might take a while the first time to build images.

You can now access the API at `http://localhost:8000`.

To interact with the Django Backend you can run `sudo docker exec -it test_api_1 bash`.
Inside the container :
```
# to enter the Virtualenv
. ./venv/bin/activate
# Now you can interact with the Django cli
./gccsite/manage.py [...]
```

To create a super user :
```
. ./venv/bin/activate
./gccsite/manage.py createsuperuser
```

# Nota Bene

[1] : If you don't use sudo while working with docker / docker-compose you have
now opened yourself to a local privilege escalation. :)
