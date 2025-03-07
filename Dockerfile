FROM python:3.10

WORKDIR /usr/src/app

RUN chmod 777 /usr/src/app
RUN apt-get -qq update
RUN apt-get -qq install -y --no-install-recommends curl git 

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


COPY . .
CMD ["bash", "start.sh"]
