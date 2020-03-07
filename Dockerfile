FROM python:2.7.16-stretch

RUN pip install virtualenv
RUN apt-get update && \
    apt-get install -y libssl-dev \
    build-essential  \
    python-dev default-libmysqlclient-dev

COPY ./Hello /app/Hello
COPY requirements.txt /app

WORKDIR /app

RUN virtualenv /app/env

RUN /app/env/bin/pip install -r requirements.txt

EXPOSE 5000
CMD [ "/app/env/bin/python","/app/Hello/app.py"]