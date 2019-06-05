# TODO: Instalar deps do SO, ex: deps para PIL
clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

migrations:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

setup: deps migrate

run:
	@python manage.py runserver 0.0.0.0:8000

# Caso use Celery
celery:
	@celery -A iepro_pdv worker -l info

shell:
	@python manage.py shell

collectstatic:
	@python manage.py collectstatic --noinput

# Caso use fabric
deploy:
	@export env_deploy=$(env)
	@fab deploy

help:
	grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
