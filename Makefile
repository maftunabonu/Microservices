install: 
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	#format file
	black *.py mylib/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib test_*.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker
	#docker run -p 0.0.0.0:8080:8080 9218cd462752
deploy:
	#deploy
	
all:	install lint format test deploy
