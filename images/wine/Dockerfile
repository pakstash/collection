ARG OWNER
FROM ghcr.io/${OWNER}/base-mesa-multiarch:latest

RUN sed -i 's/ main$/ main contrib/' /etc/apt/sources.list.d/debian.sources && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        wine \
        wine32 \
        winetricks && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
