FROM openlaw/scala-builder:0.10.0-node 

ARG USERNAME=vscode
ARG GIT_USER_NAME=ggzor
ARG GIT_USER_EMAIL=30713864+ggzor@users.noreply.github.com
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apk add --no-cache git iproute2 procps shadow \
    #
    # Create a non-root user to use
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME