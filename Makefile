build:
	docker-compose build dev web

clean:
	find . -name \*.pyc -delete

fetch:
	rm -rf data/*
	wget http://files.grouplens.org/datasets/movielens/ml-latest-small.zip -O data/ml-latest-small.zip
	unzip data/ml-latest-small.zip -d data/
	rm -f data/ml-latest-small.zip

test: clean
	docker-compose run dev pipenv run pytest
	docker-compose run dev pipenv run flake8

note:
	docker-compose run -p 8888:8888 -e PYTHONPATH=/app/ dev

serve:
	docker-compose run -p 5000:5000 web
