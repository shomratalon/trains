FROM ubuntu:18.04

WORKDIR /usr

COPY ../../.. /usr

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y curl python3-pip git

ENTRYPOINT ["python",  "/get_stats.py"]