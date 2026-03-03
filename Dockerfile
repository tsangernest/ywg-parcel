FROM python:3.12.12-slim


WORKDIR /app


RUN python3.12 -m venv /var/venv/
RUN pip install -U 'pip<25.3' pip-tools --no-cache-dir


COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir


COPY /app .
COPY /data .

