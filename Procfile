web: gunicorn mirchalsirstutorials.wsgi --log-file -
web: python manage.py collectstatic --no-input; gunicorn mirchalsirstutorials.wsgi --log-file - --log-level debug