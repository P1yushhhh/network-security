FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

# Install AWS CLI using pip (more reliable than apt-get)
RUN pip install awscli

# Install Python dependencies
RUN pip install -r requirements.txt

# Verify AWS CLI installation
RUN aws --version

CMD ["python3", "app.py"]
