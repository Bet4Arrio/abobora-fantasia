python manage.py migrate
python manage.py collectstatic --noinput 

gunicorn timesaverSys.wsgi -b 0.0.0.0:8050 --log-level debug
