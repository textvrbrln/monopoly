FROM    ubuntu:18.04
LABEL   description="This container contains an Ubuntu 18.04, Flask."
MAINTAINER  Kristian Kissling "pr@###.com"
ENV         TERM=xterm
ENV         HOME /home/flask

RUN	apt-get update && \
	apt-get install -y python3-pip python3-venv locales vim && \
	groupadd -r flask && \
	useradd -r -u 1000 -g flask flask && \
	mkdir -p /home/flask/mnp

RUN	    locale-gen de_DE.UTF-8
ENV 	LANG de_DE.UTF-8  
ENV 	LANGUAGE de_DE.UTF-8  
ENV 	LC_ALL de_DE.UTF-8  
RUN	    chown flask:flask -R /home/flask && \
        cd /home/flask/mnp
CMD	["/bin/bash", "start"]
WORKDIR /home/flask/mnp
USER 	flask

# Container bauen
# sudo docker build -t ubuntu1804/flask:1.0 .

# Container starten
# sudo docker run -ti -h Flask -v /mnp:/home/flask/mnp --name FLASK --user flask -p 127.0.0.1:5000:5000 ubuntu1804/flask:1.0

# Startskript m. Auto-Reload bei Änderungen (Debug) und Erreichbarkeit auf 127.0.0.1:5000
