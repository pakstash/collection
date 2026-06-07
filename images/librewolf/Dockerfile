FROM debian:unstable-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        extrepo && \
    extrepo enable librewolf && \
    extrepo update librewolf && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        librewolf \
        libgl1 \
        libegl1 \
        libglx-mesa0 \
        libgl1-mesa-dri \
        mesa-vulkan-drivers \
        libvulkan1 \
	libpulse0 \
        fonts-dejavu && \
    apt-get purge -y --auto-remove extrepo && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*

RUN useradd -m -u 1000 -s /bin/bash user
