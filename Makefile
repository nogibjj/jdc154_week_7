install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -cov=main test_main.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	
	#ruff check *.py mylib/*.py

extract:
	etl_query extract

transform_load: 
	etl_query transform_load

query:
	etl_query query "WITH av_super AS (SELECT Position, AVG(Superstar) as average from jdc_draft_2015 GROUP BY Position) SELECT p.Player, p.NameID, p.Superstar, p.Position, a.average FROM jdc_draft_2015 p JOIN av_super a ON p.Position = a.Position WHERE Superstar > a.average ORDER BY Position, Superstar DESC"
		
all: install lint test format deploy