FROM ghcr.io/alpine-ros/alpine-ros:noetic-bare

ARG HOME=/home/bot \
    BOT_VNC_PASSWORD=bot \
    ARDUINO_IDE_VERSION=1.8.19

ENV LANG=en_US.UTF-8 \
    PYTHONUNBUFFERED=1 \
    DISPLAY=:99 \
    TERM=xterm \
    RESOLUTION=1920x1080x24 \
    BOT_VNC_PORT=5900 \
    BOT_GROUP=bot \
    BOT_USER=bot \
    BOT_BRIDGE_LOCATION="/dev/tty.Bridge-Port" \
    BOT_BRIDGE_TCP_HOST=host.docker.internal \
    BOT_BRIDGE_TCP_PORT=7777 

RUN set -e && \
    addgroup -S ${BOT_GROUP} && \
    adduser  -h ${HOME} -S ${BOT_USER} -G ${BOT_GROUP} && \
    apk update && \
    apk add --no-cache \
        bash \
        x11vnc \
        xvfb \
        xfce4 \
        xterm \
        faenza-icon-theme \
        ros-noetic-catkin \
        python3 \
        py3-pip \
        socat \
        sudo \
        openjdk8-jre && \
    dbus-uuidgen --ensure=/etc/machine-id && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python; fi && \
    if [ ! -e /usr/bin/pip ]; then ln -sf pip3 /usr/bin/pip; fi && \
    pip install --upgrade pip wheel setuptools && \
    pip install pyserial && \
    # wget -q -O- https://downloads.arduino.cc/arduino-${ARDUINO_IDE_VERSION}-linux64.tar.xz \
    #     | tar xJC /usr/local/share && \
    # ln -s /usr/local/share/arduino-${ARDUINO_IDE_VERSION} /usr/local/share/arduino && \
    # ln -s /usr/local/share/arduino-${ARDUINO_IDE_VERSION}/arduino /usr/local/bin/arduino && \
    echo "$BOT_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER ${BOT_USER}

WORKDIR ${HOME}

RUN mkdir -p ${HOME}/.vnc && \
    x11vnc -storepasswd ${BOT_VNC_PASSWORD} ${HOME}/.vnc/passwd

COPY --chown=${BOT_GROUP}:${BOT_USER} ./serial-bridge.sh /serial-bridge
COPY --chown=${BOT_GROUP}:${BOT_USER} ./start /start

RUN chmod +x /serial-bridge /start

EXPOSE ${BOT_VNC_PORT}

CMD [ "/start" ]