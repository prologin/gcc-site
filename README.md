# GCC site

### Setup a development environment

Install `poetry` using your distribution's documentation.

You will also need `nodejs`, `yarn` and `pre-commit`. Those are not
strictly needed to develop on this project, but they will become very handy for
things like adding dependencies, or pre-commit hooks.

For those using Nix, everything is ready in the `flake.nix` file.

#### Initial setup

```sh
$ cd website
$ poetry install
$ poetry shell
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```

You can then go to http://localhost:8000/.

##### Super User creation
To create a super User :

```sh
$ cd website/
$ poetry shell
$ ./manage.py shell
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model();
>>> User.objects.create_superuser('email@prologin.org', 'password')
>>> exit
```

You can then go to http://localhost:8000/admin and login.

#### Regular usage

```sh
$ cd website
$ poetry install
$ poetry shell
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
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
$ cd website/
$ ./manage.sh loaddata fixtures/<fixture>.json # replace <fixture> with the one you want to load
```

/!\ Note that you will need to import users before importing events.

For the `users` fixture, user passwords are the same as their usernames.
