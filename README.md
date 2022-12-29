# GCC site

Since this site is primarily a front that handles all the workflow and an API
backend, most of the logic is the front. The API exposes data and verifies
permissions and soundness of the data pushed into it.

### Setup a development environment

Install `docker` and `docker-compose` using your distribution's documentation.

You will also need `poetry`, `nodejs`, `yarn` and `pre-commit`. Those are not
strictly needed to develop on this project, but they will become very handy for
things like adding dependencies, or pre-commit hooks.

For those using Nix, everything is ready in the `flake.nix` file.

#### Initial setup

```sh
# You can ignore errors about psycopg not being installed because it's missing
# local dependencies. Those are installed in Docker and not needed on your
# local machine.
$ pushd backend && poetry install && popd
$ pushd frontend && yarn install && popd
$ cd docker/
$ ./gen_secrets.sh
$ DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -p gccsite up --build
```

You can then go to http://localhost:8000/admin, which will automatically log
you in with your Prologin account. We can then make you superuser so you have
access to everything in the admin:

```sh
$ cd docker/
$ ./manage.sh shell
>>> from django.contrib.auth import get_user_model
>>> me = get_user_model().objects.get(email="joseph.marchand@prologin.org") # Replace this email with your Prologin email
>>> me.is_staff = True
>>> me.is_superuser = True
>>> me.save()
```

You can then reload http://localhost:8000/admin and you're good to go.

#### Regular usage

```sh
$ cd docker/
$ DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -p gccsite up --build
```

#### Formatting

We use `black`, `isort` and `eslint` as code formatters. They can be enabled
through a git pre-commit with the following command:

```sh
$ pre-commit install
```

#### Linting

We also use `pylint` (via `prospector`) to check for common Python errors. You
can use the following commands to check your code:

```sh
$ cd docker/
$ docker-compose -p gccsite exec backend_dev prospector --profile base
```

#### Services

##### Website

```
URL: http://localhost:8000/
To login with your Prologin account: http://localhost:8000/admin
To create a superuser:
$ cd docker && ./manage.sh createsuperuser
```

##### Adminer

```
URL: http://localhost:8010/
System: 'PostgreSQL'
User: 'gccsite_dev'
Password in: docker/secrets/postgres-passwd
Database: 'gccsite_dev'
```


#### Loading development data

Some development data is provided in the `backend/fixtures/` directory. You can
load this data in your DB by running:

``` sh
$ cd docker/
$ ./manage.sh loaddata fixtures/<fixture>.json # replace <fixture> with the one you want to load
```

/!\ Note that you will need to import users before importing events.

For the `users` fixture, user passwords are the same as their usernames.

#### Troubleshooting

If you can some problem with the API (data inconsistencies, etc), restart the
container might help. To do so:

```sh
$ cd docker/
$ docker-compose -p gccsite restart backend_dev # or frontend_dev
$ docker-compose -p gccsite restart reverse_dev
```

You need to restart `reverse_dev` after having restarted the frontend or the
backend as it depends on it.

If you need to delete the database to reset the whole thing up:

```sh
$ cd docker/
$ docker-compose -p gccsite down -v
```

And then follow the setup instructions once again.
