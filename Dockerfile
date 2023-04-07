FROM python:3.10-slim as build

WORKDIR /app

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10-slim
RUN groupadd -g 1001 python && \
    useradd -r -u 1001 -g python python

WORKDIR /app

COPY --chown=python:python --from=build /usr/app/venv ./venv
COPY --chown=python:python . .

USER 1001

ENV PATH="/usr/app/venv/bin:$PATH"

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000" ]