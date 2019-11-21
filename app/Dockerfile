FROM python:3.8-alpine

WORKDIR /workspace
COPY requirements.txt .
RUN apk add --no-cache jpeg-dev zlib-dev && \
    apk add --no-cache --virtual .build-deps build-base linux-headers && \
    pip install -r requirements.txt && \
    apk del .build-deps
COPY . .

ENTRYPOINT ["python", "image.py"]
