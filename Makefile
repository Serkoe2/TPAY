run:
	uvicorn app.main:app --reload

start_db:
	docker run -d \
	--name Tinkoff_db \
	-e POSTGRES_PASSWORD=qwerty \
	-e POSTGRES_USER=starter_kit \
	-p 5432:5432 \
	-v "$(PWD)/postgresdata":/var/lib/postgresql/data \
	postgres 

freeze:
	pip freeze > requirements.txt 

install:
	alembic init migrations
	alembic revision --autogenerate -m "Added required tables"
	alembic upgrade head

heroku_install:
	heroku run rm -rf migrations
	heroku run alembic init migrations
	heroku run  alembic revision --autogenerate -m "Added required tables"
	heroku run  alembic upgrade head

.PHONY: start start_db freeze install heroku_install