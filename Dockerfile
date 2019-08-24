FROM python:3.7.4-slim-stretch

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python3 flaskblog.py
