ARG OWNER
FROM ghcr.io/${OWNER}/base-mesa-multiarch:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        xz-utils \
        libcap2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
