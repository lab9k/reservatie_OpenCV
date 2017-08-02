# open-cv authentication

#### reservation system made with open-cv and Django

Demo: https://www.youtube.com/watch?v=giro7kRbgkc

### how to setup

* prerequisites:
  * python 2.7
  * Opencv

1. Install dependencies

    ```bash
    $ pip install -r requirements.txt
    ```

1. Setup database

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

1. Run the server

    for more info on this command, use the help argument on manage.py. or visit [the Django documentation](https://docs.djangoproject.com/en/1.11/ref/django-admin/)

    default port is 8000

    ```bash
    $ python manage.py runserver
    ```

1. go to the admin site to add rooms (
   [http://localhost:8000](http://localhost:8000) )


