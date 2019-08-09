# 🗑 ➡ ️💸 Trash to Cash

## Summary
A futures marketplace for buying and selling food waste

### What are the problems it will solve?
- Sustainability / good for environment
- Reduce food waste
- Supplement running capital
- Hedge risk

### How will it streamline or improve the current process or facilitate a new process?
Current food waste marketplaces are largely non-digital and driven by non-profit organizations or individual ag operations. Those digital solutions that do exist are primarily concerned with connecting surplus food or meals with consumers or businesses to purchase surplus meals or harvested crops at a discount. These apps do not attempt to create a marketplace for byproduct.

- GoMkt - restaurant to consumer app
- FoodMaven - app for selling excess or damaged harvest direct to consumers
- Full Harvest - marketplace for growers to sell surplus or damaged crops to businesses

### What is the product vision?
MVP will focus on buying and selling food waste. Future iterations could take in any waste output that functions as an input to another entity. For example, large companies could sell futures contracts for equipment that e-waste recyclers could then bid on.


## Technical Documentation

### Create a user

From the shell run
```
./manage.py shell
```

then in the shell run

```
from django.contrib.auth import get_user_model
get_user_model().objects.create_user('bob', password='passMass123')
```

This should create a user.

### Build the Development Environment
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

### Migrations / Data seeding

1. `cd futures/`
2. `python manage.py migrate`
3. `python manage.py loaddata products`

Data seeds go in `futures/fixtures`

If you make model changes, create new migrations with:

`python manage.py makemigrations website`

...and repeat `migrate` and `loaddata` steps.
