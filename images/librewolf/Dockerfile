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

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        extrepo && \
    extrepo enable librewolf && \
    extrepo update librewolf && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        librewolf \
        libegl1 \
        libpulse0 && \
    apt-get purge -y --auto-remove extrepo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
