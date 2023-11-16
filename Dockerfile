FROM locustio/locust
COPY ./locustfile.py /home
EXPOSE 8087