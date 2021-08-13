# solar_radi - Anshu Project

## Setup

```sh
# To create virtual environment
python -m venv venv

# To activate virtual environment
venv\Scripts\activate

# To instal the dependencies
pip install -r requirements.txt

#
cd solar_radi

# To make migrations
python manage.py makemigrations

# To migrate
python manage.py migrate

# To start the server
python manage.py runserver
```

## Commands to Deploy to Heroku

```sh
# For first time only
heroku login

# To create a new Project
heroku create

# To push the code to heroku
git push heroku main

# to migrate migrations in heroku
heroku run python manage.py migrate

# to open project
heroku open
```

### Reference for Heroku Django

- https://devcenter.heroku.com/articles/getting-started-with-python
- https://github.com/heroku/python-getting-started
