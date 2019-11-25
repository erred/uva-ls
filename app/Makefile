PYTHON := python3.8

.PHONY: aws-lambda
aws-lambda: aws-lambda-clean
	bash -c " \
	${PYTHON} -m venv aws-lambda-env && \
	source ./aws-lambda-env/bin/activate && \
	pip install -r requirements.txt && \
	deactivate && \
	cd ./aws-lambda-env/lib/python3.8/site-packages && \
	zip -r9 ../../../../aws-lambda.zip . && \
	cd ../../../.. && \
	zip -g aws-lambda.zip image.py"

.PHONY: aws-lambda-clean
aws-lambda-clean:
	rm -rf aws-lambda-env aws-lambda.zip || true

.PHONY: local-env local-env-clean
local-env:
	${PYTHON} -m venv env
	bash -c "source env/bin/activate && pip install -r requirements.txt"
local-env-clean:
	rm -rf env
