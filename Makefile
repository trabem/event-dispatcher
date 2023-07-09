.PHONY: tests
tests:
	coverage run -m pytest
	coverage report

.PHONY: cov-html
cov-html: tests
	coverage html

.PHONY: cov-xml
cov-xml: tests
	coverage xml

.PHONY: pre-commit
pre-commit:
	pre-commit run

.PHONY: format
format:
	pre-commit run --all-files
