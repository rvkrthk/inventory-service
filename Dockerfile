FROM python:3-alpine3.13
LABEL author="khaja"
LABEL organization="qualitythought"
ARG HOME_DIR='/inventory-service'
ADD . ${HOME_DIR}
ENV MYSQL_USERNAME='qtdevops'
ENV MYSQL_PASSWORD='qtdevops'
ENV MYSQL_SERVER='localhost'
ENV MYSQL_DATABASE='qtinvsrv'
EXPOSE 8080
WORKDIR ${HOME_DIR}
RUN apk add build-base
RUN apk add --update py-pip
RUN apk add py-cryptography
RUN apk add gcc musl-dev python3-dev libffi-dev libressl-dev cargo
RUN pip install cryptography
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "app.py" ]
