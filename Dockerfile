FROM debian:buster

LABEL MAINTAINER="alirezaie@sadegh.org"

RUN apt update &&\
    apt upgrade -y &&\
    apt install -y sqlite3 \
    python3 \
    python3-pip &&\
    pip3 install --upgrade pip;

COPY ./app/ /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt
RUN python3 /usr/src/app/manage.py makemigrations &&\
    python3 /usr/src/app/manage.py migrate &&\
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python3 /usr/src/app/manage.py shell &&\
    echo "yes" | python3 /usr/src/app/manage.py collectstatic;


WORKDIR /usr/src/app

CMD ["/usr/local/bin/gunicorn", "--bind", "unix:/tmp/gunicorn.sock", "sadegh_org.wsgi"]
