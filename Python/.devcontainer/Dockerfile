FROM python:3

ENV DEBIAN_FRONTEND=noninteractive

ARG USERNAME=vscode
ARG GIT_USER_NAME=ggzor
ARG GIT_USER_EMAIL=30713864+ggzor@users.noreply.github.com
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    && apt-get -y install git iproute2 procps lsb-release \
    #
    # Install pipenv
    && pip --disable-pip-version-check --no-cache-dir install pipenv\
    && rm -rf /tmp/pip-tmp \
    #
    # Create a non-root user to use
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND=