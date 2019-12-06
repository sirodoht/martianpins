FROM python:3.7.5
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    swig \
    libssl-dev \
    dpkg-dev \
    netcat \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -Ur /code/requirements.txt

WORKDIR /code
COPY . /code/
