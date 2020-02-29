FROM python:3.8

WORKDIR /srv
COPY ./requirements.txt /srv/
RUN pip install -r requirements.txt && pip install gunicorn
COPY . /srv/

EXPOSE 8080
ENTRYPOINT ["gunicorn", "--workers", "1", "--bind", "0.0.0.0:8080", "--log-level", "DEBUG", "app:app"]
