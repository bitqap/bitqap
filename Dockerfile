FROM alpine:3.14
RUN addgroup -S bitqap
RUN adduser  --disabled-password  --home /home/bitqap --ingroup bitqap bitqap
COPY . /home/bitqap/
RUN  chown -R bitqap:bitqap /home/bitqap/

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-pip bash jq vim sudo sqlite

USER bitqap
WORKDIR "/home/bitqap"
ENV ROOTDIR=/home/bitqap

RUN pip3 install --user  --no-warn-script-location -r /home/bitqap/requirements.txt