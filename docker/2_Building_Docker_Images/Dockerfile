FROM ubuntu:16.04

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install wget

COPY hello.sh /opt/hello.sh

RUN chmod +x /opt/hello.sh

ENTRYPOINT ["bash", "/opt/hello.sh"]
