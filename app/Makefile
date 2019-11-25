PYTHON := python3.8

.PHONY: clean
clean: clean-local-env clean-aws-lambda

.PHONY: local-env clean-local-env
local-env:
	${PYTHON} -m venv env-local
	bash -c "source env-local/bin/activate && pip install -r requirements.txt"
clean-local-env:
	rm -rf env-local || true

.PHONY: aws-lambda clean-aws-lambda
aws-lambda: clean-aws-lambda
	${PYTHON} -m venv env-aws-lambda
	bash -c "source ./env-aws-lambda/bin/activate && pip install -r requirements.txt"
	cd ./env-aws-lambda/lib/python3.8/site-packages && \
		zip -r9 ../../../../aws-lambda.zip . && \
		cd ../../../.. && \
		zip -g aws-lambda.zip image.py
clean-aws-lambda:
	rm -rf env-aws-lambda aws-lambda.zip || true
