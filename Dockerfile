FROM python:3.14.3-slim


WORKDIR /app


RUN python3.12 -m venv /var/venv/
RUN pip install -U pip pip-tools --no-cache-dir


COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir


COPY /app .
COPY /data .

