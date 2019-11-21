FROM python:3.8-alpine

WORKDIR /workspace
COPY requirements.txt .
RUN apk add --no-cache jpeg-dev zlib-dev gcc && \
    pip install -r requirements.txt
COPY . .

ENTRYPOINT ["python", "image.py"]
