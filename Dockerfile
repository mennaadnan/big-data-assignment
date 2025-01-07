# Use Ubuntu as the base image
FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# Create a virtual environment
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install pandas numpy seaborn matplotlib scikit-learn scipy
ENV PATH="/opt/venv/bin:$PATH"

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Copy the dataset to the container
COPY orders.csv /home/doc-bd-a1/

CMD ["bash"]
