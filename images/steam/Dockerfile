FROM debian:unstable-slim

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libgl1 \
        libgl1:i386 \
        libglx-mesa0 \
        libglx-mesa0:i386 \
        libgl1-mesa-dri \
        libgl1-mesa-dri:i386 \
        mesa-vulkan-drivers \
        mesa-vulkan-drivers:i386 \
        libvulkan1 \
        libvulkan1:i386 \
        fonts-dejavu \
	xz-utils \
        ca-certificates \
	libcap2 \
        && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 -s /bin/bash user
