FROM python:3.7.4-slim-stretch

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD python3 src/flaskblog.py
