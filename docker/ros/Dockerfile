FROM ghcr.io/alpine-ros/alpine-ros:noetic-bare

ARG HOME=/home/bot \
    BOT_VNC_PASSWORD=bot \
    BOT_VNC_PORT=5900 \
    BOT_GROUP=bot \
    BOT_USER=bot

ENV LANG=en_US.UTF-8 \
    BOT_VNC_RESOLUTION=1024x768

RUN set -e && \
    addgroup -S ${BOT_GROUP} && \
    adduser  -S ${BOT_USER} -G ${BOT_GROUP} && \
    apk update && \
    apk add --no-cache \
        bash \
        ros-noetic-catkin \
        x11vnc \
        xvfb \
        xfce4 \
        xorg-server \
        xf86-video-dummy && \
    dbus-uuidgen --ensure=/etc/machine-id

COPY ./xorg.conf    /etc/X11/xorg.conf
COPY ./xorg.conf.d  /etc/X11/xorg.conf.d

USER ${BOT_USER}

RUN mkdir -p ${HOME}/.vnc && \
    x11vnc -storepasswd ${BOT_VNC_PASSWORD} ${HOME}/.vnc/passwd && \
    cp /etc/X11/xinit/xinitrc ${HOME}/.xinitrc

WORKDIR ${HOME}

COPY --chown=${BOT_GROUP}:${BOT_USER} ./start /start
RUN chmod +x /start

EXPOSE ${BOT_VNC_PORT}

CMD [ "/start" ]