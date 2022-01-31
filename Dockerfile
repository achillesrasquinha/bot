FROM  python:3.7-alpine

LABEL maintainer=achillesrasquinha@gmail.com

ENV BOT_PATH=/usr/local/src/bot

RUN apk add --no-cache \
        bash \
        git \
    && mkdir -p $BOT_PATH

COPY . $BOT_PATH
COPY ./docker/entrypoint.sh /entrypoint.sh

WORKDIR $BOT_PATH

RUN pip install -r ./requirements.txt && \
    python setup.py install

ENTRYPOINT ["/entrypoint.sh"]

CMD ["bot"]