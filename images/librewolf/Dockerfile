ARG OWNER
FROM ghcr.io/${OWNER}/base-mesa:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        extrepo && \
    extrepo enable librewolf && \
    extrepo update librewolf && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        librewolf \
        libpulse0 \
        libavcodec-extra && \
    apt-get purge -y --auto-remove extrepo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
