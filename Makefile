
IMGZIPS := 	0xx.zip \
			1xx.zip \
			2xx.zip \
			3xx.zip \
			4xx.zip \
			5xx.zip

.PHONY: $(IMGZIPS) dl-pre download-images
$(IMGZIPS): dl-pre
	cd testdata && curl -LO https://github.com/seankhliao/uva-ls/releases/download/v0.0.0-photos.raw/$@
	cd testdata && unzip $@

dl-pre:
	-mkdir testdata
	cd testdata && curl -LO https://github.com/seankhliao/uva-ls/releases/download/v0.0.0-photos.raw/list.csv

download-images: $(IMGZIPS)
