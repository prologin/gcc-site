# GCC site

Since this site is primarily a front that handles all the workflow and
an API backend, most of the logic is the front. The API exposes data
and verifies permissions and soundness of the data pushed into it.

There's 2 ways of developing:
- Developing on the front (visual / workflow for instance)
  without modifying the backend.
  See [Working on the frontend](#working-on-the-frontend).
  If you need the backend API, see below.
- Developing on the backend and the frontend (add/fix/remove something on the API)
  See [Working on the backend](#working-on-the-backend) and [Working on the frontend](#working-on-the-frontend).
  **The recommanded method to work on the backend and the frontend is by using
  `docker-compose`. See [Advanced](#advanced).**

# Installing dependencies

Dependencies needed
- yarn
- python3
- pip
- poetry

## On Debian/Ubuntu based OS
```
apt-get update && apt-get install -y yarn python3-venv python3-pip && pip3 install poetry
```

# Working on the Backend
## First setup

In the api directory, run the following commands:
```
# Install Python dependencies (but not the current project)
poetry install --no-root
```

Then you can spawn a poetry shell (to access the created virtualenv);
```
poetry shell
# Now you can interact with the Django CLI
./gccsite/manage.py [...]
```

To create a super user :
```
./gccsite/manage.py createsuperuser
```

A fake password and email are completely okay since it's a local dev setup.
Just remember them to be able to log in the interface.
This allows you to access Django Admin (which is useful to add/modify/view data from the DB
easily).

To apply migrations (need to be run the first time and every time you do a Model change):
```
. ./venv/bin/activate
./gccsite/manage.py migrate
```

## Run
Go into `api/gccsite` and launch the following command:
```
./manage.py runserver
```

## Load data
Some dev data is provided in the `api/fixtures/` directory. You can load this data in your DB by running:
```
./manage.py <fixture>.json
```
User passwords are the same as their username.

# Working on the Frontend
## First setup

Go into `frontend` and launch `yarn install` to install dependencies locally.
This might take a while.

## Run

To launch the site (with hot reloading):
```
yarn dev
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

In the root of the project, simply run `sudo docker-compose -f docker-compose.dev.yaml up -d`[^1].
It might take a while the first time to build images.

Once it is done, you can access the frontend at `http://localhost:8080`.

[^1]: If you don't use sudo while working with docker / docker-compose you have
now opened yourself to a local privilege escalation. :)

#### Initial setup

Before you can start using the backend, you will need to run the following commands in the container.

To run commands inside the container, you need to `sudo docker-compose -f docker-compose.dev.yaml exec api bash`.

Then run the following:
```sh
python ./manage.py makemigrations  # Create migrations for the DB
python ./manage.py migrate         # Apply the migrations
python ./manage.py createsuperuser # Create a super user (to access Django admin)
```

You can now access the backend at `http://localhost:8000`.

#### Inspect the logs

To inspect the container logs (in case you encounter Django errors or something), run `sudo docker-compose -f docker-compose.dev.yaml logs`.

It is strongly advised to use the `--follow` option to inspect the logs continuously.

#### Stop the containers

To stop the containers, you can launch `sudo docker-compose -f docker-compose.dev.yaml stop` in the root directory.

#### Data persistence

The Postgres (database) files are stored on the root of the project in the `./pg-data` directory. This directory is mounted into the DB container, therefore the data is preserved even if the container is destroyed.

#### Allow port access

Note that this setup will only redirect ports to localhost. Therefore if you need to test on another device on your network, you will need to open ports on your network interface.

The easiest way to do it is to let Docker handle this for you. Edit the file `docker-compose.dev.yaml` and change ports redirections from `127.0.0.1:XXXX:XXXX` to `XXXX:XXXX`, this will redirect the container port on all interfaces of your host machine. If you want to restrict it to a single interface, simply edit the IP address from `127.0.0.1` to the IP associated with your interface (e.g. `192.168.42.42`).

You will need to recreate the containers to apply these changes: `sudo docker-compose -f docker-compose.dev.yaml up --force-recreate -d`.

#### Troubleshooting

If you can some problem with the API (data inconsistencies, etc),
removing the container and its state might help.

To do so run `sudo docker-compose -f docker-compose.dev.yaml down` in the root directory.

If you need to delete the database, remove the `./pg-data` directory.
