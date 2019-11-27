URL := http://nevers.studlab.os3.nl:8080

.PHONY: test test-console clean
clean:
	-rm out.jpeg
test: clean
	curl -L -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg" ${URL} -o out.jpeg
test-console:
	curl -L -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg" ${URL}
