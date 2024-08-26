# Use the latest Jenkins LTS base image
FROM jenkins/jenkins:lts

# Switch to root user
USER root

# Update package list and install dependencies
RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    build-essential \
    libssl-dev \
    libreadline-dev \
    zlib1g-dev \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxtst6 \
    libxss1 \
    libatspi2.0-0 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libcups2 \
    libgbm1

# Install xvfb for headless working
RUN apt-get install -y xvfb

# Clean apt cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Switch back to Jenkins user
USER jenkins

# Expose Jenkins port
EXPOSE 8080
