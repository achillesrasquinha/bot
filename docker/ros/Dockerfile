FROM ghcr.io/alpine-ros/alpine-ros:noetic-bare

RUN apk update && \
    apk add --no-cache \
        bash \
        ros-noetic-catkin \
        x11vnc

COPY ./start /start
RUN chmod +x /start

CMD [ "/start" ]