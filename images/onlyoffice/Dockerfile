ARG OWNER
FROM ghcr.io/${OWNER}/base-mesa:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gpg && \
    curl -fsSL https://download.onlyoffice.com/GPG-KEY-ONLYOFFICE | \
        gpg --dearmor -o /usr/share/keyrings/onlyoffice.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/onlyoffice.gpg] https://download.onlyoffice.com/repo/debian squeeze main" > \
        /etc/apt/sources.list.d/onlyoffice.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libice6 \
        libnss3 \
        libpulse0 \
        libsm6 \
        onlyoffice-desktopeditors && \
    apt-get purge -y --auto-remove \
        gpg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*
