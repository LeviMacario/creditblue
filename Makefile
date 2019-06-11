# TODO: Instalar deps do SO, ex: deps para PIL
clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

migrations:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

loaddata:
	@python manage.py loaddata initial_data.json

setup: deps migrate loaddata

run:
	@python manage.py runserver 0.0.0.0:8000

# Caso use Celery
celery:
	@celery -A iepro_pdv worker -l info

shell:
	@python manage.py shell

collectstatic:
	@python manage.py collectstatic --noinput

sshadd:
	@eval `ssh-agent`
	@sudo ssh-add -K ~/.ssh/id_rsa

# Caso use fabric
deploy:
	@export env_deploy=$(env)
	@fab deploy

help:
	grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
