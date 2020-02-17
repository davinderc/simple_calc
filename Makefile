init:
	pip install -r requirements.txt
	python setup.py sdist bdist_wheel

test:
	pytest

all:clean init test

clean:
	rm -rf build/
	rm -rf dist/