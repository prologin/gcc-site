# GCC site

### Setup a development environment

Install `docker` and `docker-compose` using the
[Docker Installation Guide](https://docs.docker.com/engine/install/) or your
distribution's documentation.

You will also need `poetry` and `pre-commit`. Those are not
strictly needed to develop on this project, but they will become very handy for
things like adding dependencies, or pre-commit hooks.

For those using Nix, everything is ready in the `flake.nix` file. (NOT UPDATED)

#### Initial setup

```sh
$ pushd website && poetry install && popd
$ cd docker/
$ ./gen_secrets.sh # Input the required secrets when asked
$ docker compose -p gccsite up --build # You can use the flag -d if you to detach the containers from your shell
```

You can then go to http://localhost:8000/.

#### Inserting fixtures
For the development environment to reproduce normal state, the folder
`website/fixtures/` contains several files that are used to insert test data
in the database. There are users, event centers, events, applications, etc...

To load all the fixtures, run the following command :

```sh
$ cd docker/
$ ./manage.sh loaddata fixtures/users.json fixtures/centers.json fixtures/events.json fixtures/profiles.json fixtures/applications.json
```

> /!\ The order is important, as some fixtures references other model fixtures
(we need to load users before profiles because profiles references users).

For the `users` fixture, user passwords are the same as their usernames.

E.g : `root@example.com` -> root

`root@example.com` is a superuser

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
$ docker compose -p gccsite up --build
```

#### Formatting

We use the following tools to format code:
- `ruff` for python files
- `djlint` for Django HTML template files format (and linting)
- `eslint` for JS files (this is not the case anymore, apparently)

All these tools should be run by pre-commit to ensure the well formatting of
your changes. You can install them directly using :

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
