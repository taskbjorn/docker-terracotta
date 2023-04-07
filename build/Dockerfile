# Build on the minimal Python Docker image.
FROM python:3.8-slim-buster

# Install required packages through APT.
# This step installs Git, required to clone the Terracotta repository.
RUN apt-get update && \
    apt-get install -y \
        git && \
    apt-get clean

# Clone and build the Terracotta repository.
# This step clones the Terracotta repository and install it locally through Pip.
# It also creates the directory required for the user input rasters and the
# optimised rasters.
RUN git clone https://github.com/DHI-GRAS/terracotta /terracotta && \
    cd /terracotta && \
    pip install -e . && \
    mkdir -p /terracotta/rasters /terracotta/optimized

# Set the working directory.
WORKDIR /terracotta

# Expose the Terracotta server ports.
EXPOSE 5000 5100

# Copy the entrypoint script.
COPY entrypoint.py /

# Launch the entrypoint script on startup.
CMD ["python3", "/entrypoint.py"]