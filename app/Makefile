PYTHON := python3.8

.PHONY: clean
clean: clean-awslambda clean-gcpfunctions clean-ibmfunctions

.PHONY: awslambda clean-awslambda
awslambda: clean-awslambda
	cd ./awslambda/env/lib/python3.8/site-packages && \
		zip -r9 ../../../../../awslambda.zip . && \
		cd ../../../.. && \
		zip -g ../awslambda.zip awslambda.py
clean-awslambda:
	-rm -rf awslambda.zip

.PHONY: gcpfunctions clean-gcpfunctions
gcpfunctions: clean-gcpfunctions
	cd gcpfunctions && zip -r9 ../gcpfunctions.zip *
clean-gcpfunctions:
	-rm -rf gcpfunctions.zip

.PHONY: ibmfunctions clean-ibmfunctions
ibmfunctions: clean-ibmfunctions
	cd ibmfunctions && zip -r9 ../ibmfunctions.zip *
clean-ibmfunctions:
	-rm -rf ibmfunctions.zip

.PHONY: docker docker-pypy
docker:
	docker build -t ls-server:latest docker
docker-pypy:
	docker build -t ls-server-pypy docker-pypy
