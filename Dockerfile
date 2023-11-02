FROM python:3.11

RUN echo > /root/.bashrc

# Adds a custom command prompt to the docker container.
RUN echo "PS1='🐳\[\033[01;32m\]\u@:\[\033[01;34m\]\W\[\033[00m\] \$ '" >> /root/.bashrc

# Makes default `ls` display colors.
RUN echo "alias ls='ls --color=auto'" >> /root/.bashrc

WORKDIR /app/exercises
ENTRYPOINT ["/bin/bash"]
