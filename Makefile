format: 
	poetry run black cards tests

test: 
	poetry run pytest

cov: 
	poetry run pytest --cov-report html --cov=cards tests && open htmlcov/index.html