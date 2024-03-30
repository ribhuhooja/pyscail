# build automation

build:
	python3 -m build
	twine upload dist/*

unbuild:
	rm -rf dist/*
	
upgrade:
	pip install --upgrade pyscail
