URL := http://nevers.studlab.os3.nl:8080

.PHONY: test test-console clean
clean:
	-rm out.jpeg
test: clean
	curl -L -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg" ${URL} -o out.jpeg
test-console:
	curl -L -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg" ${URL}
test-gcp-run: clean
	curl -L -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg" https://ls-project-image-6jdjoh342a-ew.a.run.app  -o out.jpeg

test-gcp-fun: clean
	curl -L -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg" https://europe-west1-cedar-channel-259712.cloudfunctions.net/ls-benchmark -o out.jpeg

test-zeitnow: clean
	curl -L -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg" https://zeitnow.lsproject.now.sh/api/zeit  -o out.jpeg

test-azure: clean
	curl -L -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg"  https://ls-benchmark.azurewebsites.net/api/ls-project?code=WQxbpOmKFASyfrtGTmHM6SFJoSvw8EXJHncfUX3C/an7FpVT7UvF4Q==  -o out.jpeg
