FROM python:alpine3.14
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
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "app.py" ]