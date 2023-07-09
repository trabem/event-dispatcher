.PHONY: unittests
unittests:
	coverage run -m pytest

.PHONY: tests
tests: unittests
	coverage report

.PHONY: cov-html
cov-html: unittests
	coverage html

.PHONY: cov-xml
cov-xml: unittests
	coverage xml

.PHONY: pre-commit
pre-commit:
	pre-commit run

.PHONY: format
format:
	pre-commit run --all-files