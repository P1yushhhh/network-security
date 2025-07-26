FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

# Install system dependencies and AWS CLI v2
RUN apt-get update -y && \
    apt-get install -y curl unzip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws/ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install -r requirements.txt

# Verify AWS CLI installation
RUN aws --version

CMD ["python3", "app.py"]
