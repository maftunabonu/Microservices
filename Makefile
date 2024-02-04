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
	python -m pytest -vv --cov=mylib test_logic.py
deploy:
	#deploy
all:	install lint format test deploy
