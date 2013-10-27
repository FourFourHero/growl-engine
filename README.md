Run the server
	python manage.py runserver

Schema migrations

	python manage.py schemamigration growl --auto
	python manage.py migrate growl
	
Celery tasks

	python manage.py celery worker -B --loglevel=debug