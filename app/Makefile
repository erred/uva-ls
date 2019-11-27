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
	${PYTHON} -m venv awslambda/env
	bash -c "cd awslambda && source ./env/bin/activate && pip install -r requirements.txt"
	cd ./awslambda/env/lib/python3.8/site-packages && \
		zip -r9 ../../../../../awslambda.zip . && \
		cd ../../../.. && \
		zip -g ../awslambda.zip awslambda.py
clean-aws-lambda:
	rm -rf awslambda/env awslambda.zip || true

.PHONY: gcp-functions
gcp-functions: gcp-functions-clean
	cd gcpfunctions && zip -r9 ../gcpfunctions.zip *
gcp-functions-clean:
	rm -rf gcpfunctions.zip || true
