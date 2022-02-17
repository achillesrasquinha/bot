FROM ghcr.io/alpine-ros/alpine-ros:noetic-ros-core

ARG HOME=/home/bot \
    BOT_VNC_PASSWORD=bot

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    PYTHONUNBUFFERED=1 \
    DISPLAY=:99 \
    TERM=xterm \
    RESOLUTION=1920x1080x24 \
    BOT_VNC_PORT=5900 \
    BOT_HOST=ros \
    BOT_PORT=8080 \
    BOT_SOCKET_PORT=3000 \
    BOT_GROUP=bot \
    BOT_USER=bot \
    BOT_BRIDGE_LOCATION="/dev/tty.Bridge-Port" \
    BOT_BRIDGE_TCP_HOST=host.docker.internal \
    BOT_BRIDGE_TCP_PORT=7777 \
    ROS_PACKAGE_PATH=/home/bot/catkin_ws/src \
    DPYTHON_EXECUTABLE=/usr/bin/python3 \
    WEBSOCKIFY_VERSION=0.10.0 \
    ROS_DISTRO=noetic \
    ROS_CORE_PORT=13111 \
    ROS_MASTER_URI=http://ros:13111

RUN set -e && \
    addgroup -S ${BOT_GROUP} && \
    adduser  -h ${HOME} -S ${BOT_USER} -G ${BOT_GROUP} && \
    apk update && \
    apk add --no-cache \
        bash \
        git \
        xhost \
        x11vnc \
        xvfb \
        xfce4 \
        xterm \
        faenza-icon-theme \
        python3 \
        py3-pip \
        socat \
        make \
        gcc \
        g++ \
        sudo \
        ros-${ROS_DISTRO}-turtlesim \
        openrc \
        lightdm \
        dbus && \
    dbus-uuidgen --ensure=/etc/machine-id && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python; fi && \
    if [ ! -e /usr/bin/pip ]; then ln -sf pip3 /usr/bin/pip; fi && \
    pip install --upgrade pip wheel "setuptools<50" && \
    pip install \
        pyserial \
        git+https://github.com/achillesrasquinha/bpyutils.git@develop && \
    # git clone --depth 1 https://github.com/achillesrasquinha/bot.git /bot && \
    # cd /bot && \
    # pip3 install -r ./requirements.txt --use-deprecated=legacy-resolver && \
    # python3 setup.py install && \
    echo "$BOT_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    git clone --depth 1 https://github.com/novnc/noVNC.git /noVNC && \
    git clone --depth 1 https://github.com/novnc/websockify /noVNC/utils/websockify && \
    rm -rf /noVNC/.git && \
    rm -rf /noVNC/utils/websockify/.git && \
    apk del git && \
    sed -i -- "s/ps -p/ps -o pid | grep/g" /noVNC/utils/novnc_proxy && \
    cp /noVNC/vnc.html /noVNC/index.html && \
    # change default shell from ash to bash
    sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd && \
    echo "source $HOME/catkin_ws/devel/setup.sh" >> $HOME/.bashrc && \
    rc-update add dbus && \
    rc-update add lightdm

COPY ./socket-app /app
RUN cd /app && \
    pip install -r ./requirements.txt

USER ${BOT_USER}

WORKDIR ${HOME}

RUN mkdir -p ${HOME}/.vnc && \
    x11vnc -storepasswd ${BOT_VNC_PASSWORD} ${HOME}/.vnc/passwd && \
    touch ${HOME}/.Xauthority
    
COPY --chown=${BOT_GROUP}:${BOT_USER} ./serial-bridge.sh /serial-bridge
COPY --chown=${BOT_GROUP}:${BOT_USER} ./socket-bridge /socket-bridge
COPY --chown=${BOT_GROUP}:${BOT_USER} ./start /start

RUN chmod +x /serial-bridge /socket-bridge /start
    # && \
    # mkdir -p ${HOME}/catkin_ws/src && \
    # mkdir -p ${HOME}/shared && \
    # ln -sf ${HOME}/shared/catkin_ws ${HOME}/catkin_ws && \
    # sudo chown ${BOT_GROUP}:${BOT_USER} ${HOME}/catkin_ws && \
    # sudo chown ${BOT_GROUP}:${BOT_USER} ${HOME}/shared

CMD [ "/start" ]