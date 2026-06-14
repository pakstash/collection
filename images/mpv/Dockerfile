ARG OWNER
FROM ghcr.io/${OWNER}/base-mesa:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        mpv \
        python3-pip \
        libpulse0 \
        ffmpeg && \
    pip3 install --no-cache-dir --break-system-packages yt-dlp && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
