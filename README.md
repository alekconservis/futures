# Application name here
Description of application goes here...

## Create a user

From the shell run
```
./manage.py shell
```

then in the shell run

```
from django.contrib.auth import get_user_model
get_user_model().objects.create_user('bob', passwor='passMass123')
```

This should create a user.

## Build the Development Environment
To create your python environment simply run
```
make build_env
```
from this repositories base directory and then run
```
source env/bin/activate
```
This will activate the virtual environment created
in the first line of code. All development should
performed using this environment to ensure that the
results of your code can be reproduced by other contributors.

## Migrations / Data seeding

1. `cd futures/`
2. `python manage.py migrate`
3. `python manage.py loaddata products`

Data seeds go in `futures/fixtures`

If you make model changes, create new migrations with:

`python manage.py makemigrations website`

...and repeat `migrate` and `loaddata` steps.
