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

https://warm-6jdjoh342a-ew.a.run.app/
https://cold-6jdjoh342a-ew.a.run.app/

test-gcp-fun: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" https://europe-west1-cedar-channel-259712.cloudfunctions.net/ls-benchmark -o ${OUTFILE}

https://us-central1-cedar-channel-259712.cloudfunctions.net/cold
https://us-central1-cedar-channel-259712.cloudfunctions.net/warm


test-zeitnow: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" https://zeitnow.lsproject.now.sh/api/zeit  -o ${OUTFILE}

https://warm.lsproject.now.sh
https://cold.lsproject.now.sh

test-azure: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" https://lsproject.azurewebsites.net/api/lsbenchmark -o ${OUTFILE}

https://lsproject.azurewebsites.net/api/cold
https://lsproject.azurewebsites.net/api/warm

test-ibm: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg" https://eu-gb.functions.cloud.ibm.com/api/v1/web/marbadias97%40gmail.com_dev/default/ls-benchmark  -o ${OUTFILE}

https://eu-gb.functions.cloud.ibm.com/api/v1/web/marbadias97%40gmail.com_dev/default/warm
https://eu-gb.functions.cloud.ibm.com/api/v1/web/marbadias97%40gmail.com_dev/default/cold

test-awslambda: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg"  --header "Accept: image/jpeg" https://l9u9mkqc9b.execute-api.us-east-2.amazonaws.com/default/ls-server -o ${OUTFILE}

https://xt8gn4dt7g.execute-api.eu-west-2.amazonaws.com/default/warm
https://wo3u7x3tt8.execute-api.eu-west-2.amazonaws.com/default/cold


test-alicloud: clean
	curl -L -v --data-binary ${INFILE} --header "Content-Type: image/jpeg"  --header "Accept: image/jpeg"  https://5055975195697149.eu-central-1.fc.aliyuncs.com/2016-08-15/proxy/alicloudfunctions/alicloudfunctions/ -o ${OUTFILE}

https://5055975195697149.eu-central-1.fc.aliyuncs.com/2016-08-15/proxy/cold/cold/
https://5055975195697149.eu-central-1.fc.aliyuncs.com/2016-08-15/proxy/warm/warm/
