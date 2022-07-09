FROM python:3.10.5-bullseye

# Install gcc for pip package compilation
RUN apt-get install -y gcc

# Install locust
# RUN pip install psutil pyzmq locust faker
RUN pip install locust

# Cleanup after install
RUN rm -rf /var/lib/apt/lists/*

ADD locustfile.py /config/locustfile.py
ADD runLocust.sh /usr/local/bin/runLocust.sh

ENV LOCUST_FILE /config/locustfile.py

EXPOSE 8089

ENTRYPOINT ["/usr/local/bin/runLocust.sh"]
