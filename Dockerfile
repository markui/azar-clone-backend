# Base Image
FROM        viking617/base
MAINTAINER  viking617617@gmail.com

# Django Settings
ENV         LANG C.UTF-8
ENV         DJANGO_SETTINGS_MODULE config.settings.local

# 파일 복사 및 requirements 설치
COPY        . /srv/app
RUN         /root/.pyenv/versions/app/bin/pip install -r /srv/app/requirements.txt

# pyenv local 설정
WORKDIR     /srv/app
RUN         pyenv local app

RUN         cp .config/nginx/nginx.conf \
                /etc/nginx/nginx.conf
# Nginx
RUN         cp .config/nginx/nginx.conf \
                /etc/nginx/nginx.conf
RUN         cp .config/nginx/app.conf \
                /etc/nginx/sites-available/
RUN         rm -rf /etc/nginx/sites-enabled/*
RUN         ln -sf /etc/nginx/sites-available/app.conf \
                    /etc/nginx/sites-enabled/app.conf

# log directory
RUN         mkdir -p /var/log/uwsgi/app

# manage.py - collect staticfiles, DB migration
#WORKDIR     /srv/app/azar
#RUN         /root/.pyenv/versions/app/bin/python manage.py collectstatic --noinput
#RUN         /root/.pyenv/versions/app/bin/python manage.py migrate --noinput

# supervisor
RUN         cp .config/supervisor/* \
                /etc/supervisor/conf.d/
CMD         supervisord -n

EXPOSE      80 8013