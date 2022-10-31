format:
	black *.py --line-length 79

test:
	python3 -m pytest test/

lint:
	flake8 *.py

clean:
	rm -rf __pycache__

