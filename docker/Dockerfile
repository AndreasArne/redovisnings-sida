FROM python:3.5-alpine

RUN adduser -D deploy

WORKDIR /home/deploy

COPY requirements/prod.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY me_page.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP me_page.py

RUN chown -R deploy:deploy ./
USER deploy

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
