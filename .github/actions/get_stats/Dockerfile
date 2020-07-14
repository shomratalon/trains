FROM ubuntu:18.04

WORKDIR /usr

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y curl python3-pip git

ENTRYPOINT ["python3",  ".github/actions/get_stats/get_stats.py"]
CMD tail -f /dev/null