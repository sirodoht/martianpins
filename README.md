# martianpins

[IPFS](https://ipfs.io/) pinning service.

![screenshot](screenshot.png)

## Development

This is a [Django](https://www.djangoproject.com/) codebase. Check out the 
[Django docs](https://docs.djangoproject.com/) for general technical documentation.

### Structure

The Django project is [`martianpins`](/martianpins). There is one Django app,
[`main`](/main) Django app, with all business logic.

### Dependencies

Create virtualenv, enable it and then install requirements:
```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

> Note: This project uses [pip-tools](https://github.com/jazzband/pip-tools) for dependencies management.

### Environment variables

You need to create a new file named `.env` in the root of this project once you cloned it.

`.env` should contain the following env variables:
```
SECRET_KEY="thisisthesecretkey"
DATABASE_URL="postgres://postgres:postgres@127.0.0.1:5432/martianpins"
EMAIL_HOST_USER="smtp_user"
EMAIL_HOST_PASSWORD="smtp_password"
DEFAULT_FROM_EMAIL="Marvin von Martian Pins <marvin@martianpins.com>"
IPFS_NODE_URL="https://ipfs.martianpins.com"
SENTRY_DSN="https://0123456b805246cc3c200b97132114rc@sentry.io/000111"
```

### Database

This project uses PostgreSQL. See above on how to configure it using the `.env` file.

> [How to: PostgreSQL on Docker](https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198)

After creating your local database, you need to apply the migrations:
```sh
python manage.py migrate
```

### Serve

Finally, you can run the Django development server:
```sh
python manage.py runserver
```

Or, run the production-grade `uwsgi` server:
```sh
uwsgi --ini=uwsgi.ini
```

> Note: The `uwsgi` method does not read the `.env` file, so in this case you need to set the env vars in your shell.

## Deployment

martianpins needs an IPFS node to work (defined in the `.env` file -- see section "Environment variables").
Running an IPFS node might not be the easiest and most predictable thing, so take a look at many articles like
[this one](https://medium.com/@rossbulat/introduction-to-ipfs-set-up-nodes-on-your-network-with-http-gateways-10e21ea689a4)
before you attempt it.

## Code linting & formatting

```sh
black . && isort -y && flake8
```
