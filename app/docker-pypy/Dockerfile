FROM pypy:3

WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["pypy3", "image.py"]
