# GCC site

### Setup a development environment

Install `docker` and `docker-compose` using your distribution's documentation.

You will also need `poetry`, `nodejs`, `yarn` and `pre-commit`. Those are not
strictly needed to develop on this project, but they will become very handy for
things like adding dependencies, or pre-commit hooks.

For those using Nix, everything is ready in the `flake.nix` file.

#### Initial setup

```sh
$ pushd backend && poetry install && popd
$ cd docker/
$ ./gen_secrets.sh
$ DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -p gccsite up --build
```

You can then go to http://localhost:8000/.

##### Super User creation
To create a super User :

```sh
$ cd docker/
$ ./manage.sh createsuperuser
# Then follow the given instructions.
```

You can then go to http://localhost:8000/admin and login.

#### Regular usage

```sh
$ cd docker/
$ DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -p ndf up --build
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
$ docker-compose -p gccsite exec website_dev prospector --profile base
```

#### Loading development data

Some development data is provided in the `website/fixtures/` directory. You can
load this data in your DB by running:

``` sh
$ cd docker/
$ ./manage.sh loaddata fixtures/<fixture>.json # replace <fixture> with the one you want to load
```

/!\ Note that you will need to import users before importing events.

For the `users` fixture, user passwords are the same as their usernames.
