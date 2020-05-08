FROM python:3.8-buster

LABEL MAINTAINER="alirezaie@sadegh.org"

WORKDIR /usr/src/app

COPY ./app/ /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt
RUN python3 /usr/src/app/manage.py makemigrations &&\
    python3 /usr/src/app/manage.py migrate &&\
    python3 manage.py migrate --run-syncdb &&\
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python3 /usr/src/app/manage.py shell &&\
    echo "yes" | python3 /usr/src/app/manage.py collectstatic;

CMD ["/usr/local/bin/gunicorn", "--bind", "unix:/tmp/gunicorn.sock", "-w", "4", "sadegh_org.wsgi"]
