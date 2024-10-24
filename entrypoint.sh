python manage.py migrate
python manage.py collectstatic --noinput 

gunicorn fantasy.wsgi -b 0.0.0.0:8051 --log-level debug
