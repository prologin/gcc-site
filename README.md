# GCC site

Since this site is primarily a front that handles all the workflow and
an API backend, most of the logic is the front. The API exposes data
and verifies permissions and soundness of the data pushed into it.

There's 2 ways of developing:
- Developing on the front (visual / workflow for instance)
  without modifying the backend.
  See # Working on the frontend
  If you need the backend API, see below.
- Developing on the backend and the frontend (add/fix/remove something on the API)
  See # Working on the backend and # Working on the frontend

# Installing dependencies

Dependencies needed
- yarn
- pip
- python3

## On Debian/Ubuntu based OS
```
apt-get update && apt-get install -y yarn python3-venv python3-pip
```

# Working on the Backend
## First setup

In the api directory, run the following commands:
```
# Create an "isolated environment" where you can install python packages
python3 -m venv venv
# Activate this environment
. ./venv/bin/activate
# Install python packages
pip3 install -r requirements.txt
```

Create the file gccsite/gccsite/settings/dev.py (it's a gitignored file)
containing the following:

```
from .common import * # noqa

SOCIAL_AUTH_PROLOGIN_KEY = (
    "FIXME" # Replace with a random string
)

SOCIAL_AUTH_PROLOGIN_SECRET = (
    "FIXME" # Replace with a random string
)
```

If you want the real values (to be able to use Prologin OIDC), ask a root :).

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
A fake password and email are completely okay since it's a local dev setup.
Just remember them to be able to log in the interface.
This allows you to access Django Admin (which is useful to add/modify/view data from the DB
easily).

To apply migrations (need to be run the first time and every time you do a Model change) :
```
. ./venv/bin/activate
./gccsite/manage.py migrate
```

## Run
Go into `api/gccsite` and launch the following command:
```
./manage.py runserver
```

You might have the create the migrations / apply them.
See the Django documentation : https://docs.djangoproject.com/en/4.0/topics/migrations/

# Working on the Frontend
## First setup

Go into `front` and launch `yarn install` to install dependencies locally.
This might take a while.

## Run

To launch the site (with hot reloading):
```
yarn serve
```

You can now access the front at `http://localhost:8080`.

# Advanced

Docker-compose can be used when you want to work on the front and need a running API.

## Backend docker-compose

See `https://docs.docker.com/engine/install/` :).

### Install Docker-Compose

See `https://docs.docker.com/compose/install/` :)
Select `Linux` and proceed with installation.

/!\ Be careful NOT TO use `pip` to install docker-compose system-wise.
This is almost certain to break your system.

### Docker compose usage

Go into ./test and launch `sudo docker-compose up -d` [1].
It might take a while the first time to build images.

You can now access the API at `http://localhost:8000`.

Go into `front` and launch `yarn serve` to launch the server for VueJS and
code hot reloading. (This makes developing much easier).

You can now access the front at `http://localhost:8080`.

To stop the containers, you can launch `docker-compose down` in the test directory.

To interact with the Django Backend you can run `sudo docker exec -it dev-setup_api_1 bash`.
You can use the same commands as the Backend first setup above.

Note that the state is inside the container as a sqlite DB. Thus if you remove the container,
the state will disappear and you will have to do the first setup again.

[1] : If you don't use sudo while working with docker / docker-compose you have
now opened yourself to a local privilege escalation. :)

### Troubleshooting

If you can some problem with the API (data inconsistencies, etc),
removing the container and its state might help.

To do so run `docker-compose destroy` in the test directory.
Note that all backend data will be deleted.

If you want to save some data for tests, you should add fixtures to the backend.

