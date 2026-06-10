FROM debian:unstable-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        libegl1 \
        libgl1 \
        libglx-mesa0 \
        libgl1-mesa-dri \
        mesa-vulkan-drivers \
        libvulkan1 \
        fonts-dejavu && \
    useradd -m -u 1000 -s /bin/bash user && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
