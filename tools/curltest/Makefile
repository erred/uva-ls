URL := http://nevers.studlab.os3.nl:8080

INFILE := "@chrome2x.jpg"
OUTFILE := out.jpg

clean:
	-rm ${OUTFILE}

test-console:
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" ${URL}

test: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" ${URL} -o ${OUTFILE}

test-gcp-run: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" https://ls-project-image-6jdjoh342a-ew.a.run.app  -o ${OUTFILE}

test-gcp-fun: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" https://europe-west1-cedar-channel-259712.cloudfunctions.net/ls-benchmark -o ${OUTFILE}

test-zeitnow: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" https://zeitnow.lsproject.now.sh/api/zeit  -o ${OUTFILE}

test-azure: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg"  https://ls-benchmark.azurewebsites.net/api/ls-project?code=WQxbpOmKFASyfrtGTmHM6SFJoSvw8EXJHncfUX3C/an7FpVT7UvF4Q==  -o ${OUTFILE}

test-ibm: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg"  https://eu-gb.functions.cloud.ibm.com/api/v1/web/marbadias97%40gmail.com_dev/default/ls-benchmark  -o ${OUTFILE}

