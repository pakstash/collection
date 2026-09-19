ARG OWNER
FROM ghcr.io/${OWNER}/base-mesa-multiarch:latest AS build

ARG UMU_VERSION=1.4.4

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        bash \
        build-essential \
        ca-certificates \
        cargo \
        git \
        libzstd-dev \
        python3-build \
        python3-dev \
        python3-hatch-vcs \
        python3-hatchling \
        python3-installer \
        python3-pip \
        python3-setuptools \
        python3-setuptools-scm \
        python3-wheel \
        scdoc && \
    git clone --branch "${UMU_VERSION}" --depth 1 --recurse-submodules --shallow-submodules \
        https://github.com/Open-Wine-Components/umu-launcher.git /build/umu-launcher && \
    cd /build/umu-launcher && \
    ./configure.sh --prefix=/usr && \
    make -j"$(nproc)" && \
    make DESTDIR=/build/root install

ARG OWNER
FROM ghcr.io/${OWNER}/base-mesa-multiarch:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libzstd1 \
        python3 \
        python3-cbor2 \
        python3-truststore \
        python3-xlib \
        python3-xxhash \
        xz-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /run/* /tmp/*

COPY --from=build /build/root /
