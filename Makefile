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

.PHONY: start start_db freeze