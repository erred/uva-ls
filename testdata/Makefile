URL := http://nevers.studlab.os3.nl:8080

.PHONY: test
test:
	curl -v --data-binary "@chrome2x.jpg" --header "Content-Type: image/jpeg" ${URL} -o out.jpeg
