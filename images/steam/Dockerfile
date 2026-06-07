FROM debian:unstable-slim AS common

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        libgl1 \
        libglx-mesa0 \
        libgl1-mesa-dri \
        mesa-vulkan-drivers \
        libvulkan1 \
        fonts-dejavu && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*

RUN useradd -m -u 1000 -s /bin/bash user

FROM common

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libgl1:i386 \
        libglx-mesa0:i386 \
        libgl1-mesa-dri:i386 \
        mesa-vulkan-drivers:i386 \
        libvulkan1:i386 \
        xz-utils \
        libcap2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
