all:	init

init:
	pip install -r requirements.txt

test:
	nosetests -v

clean:
	rm -fv *.pyc
	rm -fv tests/*.pyc
