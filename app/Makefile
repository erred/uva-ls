PYTHON := python3.8

.PHONY: clean
clean: clean-awslambda clean-gcpfunctions

.PHONY: local-env clean-local-env
local-env:
	bash -c "source env-local/bin/activate && pip install -r requirements.txt"

.PHONY: awslambda clean-awslambda
awslambda: clean-awslambda
	cd ./awslambda/env/lib/python3.8/site-packages && \
		zip -r9 ../../../../../awslambda.zip . && \
		cd ../../../.. && \
		zip -g ../awslambda.zip awslambda.py
clean-awslambda:
	rm -rf awslambda/env awslambda.zip || true

.PHONY: gcp-functions clean-gcpfunctions
gcpfunctions: clean-gcpfunctions
	cd gcpfunctions && zip -r9 ../gcpfunctions.zip *
clean-gcpfunctions:
	rm -rf gcpfunctions.zip || true
