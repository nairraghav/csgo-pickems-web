format:
	black src/ --line-length 79
	black test/ --line-length 79

test:
	python3 -m pytest test/

lint:
	flake8 src/
	flake8 test/

clean:
	rm -rf __pycache__

install:
	pip install -r requirements.txt

run:
	python src/pickems.py