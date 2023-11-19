# project_template_default# Celeri WebApp
initial repository for the Celeri webapp

<br/>


## Development 

To get started:

0. clone the repo and cd into the directory:
```git clone git@github.com:davidslusser/celeri.git```

1. create virtual environment and enable:
```python -m venv venv```

2. activate the virtual env
```source venv/bin/activate```

3. install the python requirements:
```pip install .[dev]```

4. cd to the django_project directory
```cd django_project```

5. run migrations (creates the database):
```python manage.py migrate```

6. create an admin user:
```python manage.py add_superuser --group admin```

7. start the local demo server:
```python manage.py runserver```

8. log in to the locally running system at: http://127.0.0.1:8000

    - login with admin/admin
    - navigate to http://127.0.0.1:8000/admin to play with data

<br/>

### To 'reset' your local data

- delete the database file:
```rm db.sqlite3```
- re-run the migrate command:
```python manage.py migrate```
- generate some local test data:
```python manage.py generate_data```