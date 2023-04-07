FROM docker.io/library/python:3.12.0a5-slim

RUN groupadd -g 1001 python && \
    useradd -r -u 1001 -g python python
USER 1001

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000" ]
