build:
	rm -rf dist/
	python -m build
	python -m twine upload --repository testpypi dist/* --verbose
