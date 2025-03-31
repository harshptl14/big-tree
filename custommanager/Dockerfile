FROM bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8

MAINTAINER Harsh Patel <your-email@example.com>

# Install Python 3
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Verify Python installation
RUN python3 --version