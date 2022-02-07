FROM osrf/ros:noetic-desktop-full-buster

LABEL maintainer Achilles Rasquinha achillesrasquinha@gmail.com

ARG HOME=/home/bot \
    BOT_GROUP_ID=1001 \
    BOT_GROUP=bot \
    BOT_USER_ID=1001 \
    BOT_USER=bot \
    BOT_VNC_PASSWORD=bot \
    ARDUINO_IDE_VERSION=1.8.19 \
    LANG=C

ENV LANG=${LANG}.UTF-8 \
    LC_ALL=${LANG}.UTF-8 \
    LANGUAGE=${LANG}:UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    DISPLAY=:99 \
    RESOLUTION=1920x1080x24 \
    TERM=xterm \
    BOT_GROUP=${BOT_GROUP} \
    BOT_USER=${BOT_USER} \
    BOT_VNC_PORT=5900 \
    BOT_BRIDGE_LOCATION="/dev/tty.Bridge-Port" \
    BOT_BRIDGE_TCP_HOST=host.docker.internal \
    BOT_BRIDGE_TCP_PORT=7777 \
    ROS_DISTRO=noetic \
    ROS_PACKAGE_PATH=${HOME}/catkin_ws/src \
    DPYTHON_EXECUTABLE=/usr/bin/python3 \
    ROS_CORE_PORT=11311

RUN set -e && \
    groupadd -g ${BOT_GROUP_ID} ${BOT_GROUP} && \
    useradd -rm -d ${HOME} -s /bin/bash -g ${BOT_GROUP} -G sudo -u ${BOT_USER_ID} ${BOT_USER} && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        xvfb \
        xfce4 \
        x11vnc \
        dbus-x11 \
        xterm \
        papirus-icon-theme \
        python3 \
        python3-pip \
        socat && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python; fi && \
    if [ ! -e /usr/bin/pip ]; then ln -sf pip3 /usr/bin/pip; fi && \
    pip install --upgrade pip wheel setuptools && \
    pip install \
        pyserial \
        git+https://github.com/achillesrasquinha/bpyutils.git@develop#egg=bpyutils && \
    echo "$BOT_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    rm -rf /var/lib/apt/lists/* && \
    echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ${HOME}/.bashrc

USER ${BOT_USER}

WORKDIR ${HOME}

RUN mkdir -p ${HOME}/.vnc && \
    x11vnc -storepasswd ${BOT_VNC_PASSWORD} ${HOME}/.vnc/passwd

COPY --chown=${BOT_GROUP}:${BOT_USER} ./serial-bridge.sh /serial-bridge
COPY --chown=${BOT_GROUP}:${BOT_USER} ./start /start

RUN chmod +x /serial-bridge /start && \
    mkdir -p ${HOME}/catkin_ws/src

EXPOSE ${BOT_VNC_PORT}

CMD [ "/start" ]