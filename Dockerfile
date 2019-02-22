FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
#  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install build-essential
COPY requirements.txt /src/requirements/requirements.txt
RUN pip3 install -r /src/requirements/requirements.txt
RUN echo exit 0 > /usr/sbin/policy-rc.d

RUN groupadd -g 999 pyasynch && \
    useradd -r -u 999 -g pyasynch pyasynch
USER pyasynch