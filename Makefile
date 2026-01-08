# ==========================
# Configuration
# ==========================

PRJECT_NAME=django app
COMPOSE=docker-compose
WEB_SERVICE=web
DJANGO_PORT=8000
DJANGO_URL=http://localhost:$(DJANGO_PORT)


# ==========================
# Docker lifecycle
# ==========================

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

restart:
	$(COMPOSE) down
	$(COMPOSE) up -d

logs:
	$(COMPOSE) logs -f

# ==========================
# Django commands
# ==========================

shell:
	$(COMPOSE) exec $(WEB_SERVICE) bash

django_shell:
	$(COMPOSE) exec -it $(WEB_SERVICE) python manage.py shell

migrate:
	$(COMPOSE) exec $(WEB_SERVICE) python manage.py migrate

makemigrations:
	$(COMPOSE) exec $(WEB_SERVICE) python manage.py makemigrations

superuser:
	$(COMPOSE) exec -it $(WEB_SERVICE) python manage.py createsuperuser


collectstatic:
	$(COMPOSE) exec $(WEB_SERVICE) python manage.py collectstatic --noinput

test:
	$(COMPOSE) exec $(WEB_SERVICE) python manage.py test

# ==========================
# Cleanup
# ==========================

clean:
	$(COMPOSE) down -v