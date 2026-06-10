ARG OWNER
FROM ghcr.io/${OWNER}/base-mesa:latest

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libegl1:i386 \
        libgl1:i386 \
        libglx-mesa0:i386 \
        libgl1-mesa-dri:i386 \
        mesa-vulkan-drivers:i386 \
        libvulkan1:i386 \
        xz-utils \
        libcap2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
