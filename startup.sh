python manage.py migrate
gunicorn --workers 4 --timeout 60 --bind=0.0.0.0 --chdir=/home/site/wwwroot ChurnShield.wsgi --access-logfile '-' --error-logfile '-'
