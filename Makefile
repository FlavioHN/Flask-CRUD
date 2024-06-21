run:
	flask run

create-migrations:
	flask db revision --autogenerate

run-migrations:
	flask db upgrade head