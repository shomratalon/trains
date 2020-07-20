FROM ubuntu:18.04

WORKDIR /usr

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y curl python3-pip git
RUN pip3 install github3.py
RUN pip3 install trains
RUN pip3 install pandas
RUN pip3 install tabulate

ENTRYPOINT ["python3",  ".github/actions/get_stats/get_stats.py"]
