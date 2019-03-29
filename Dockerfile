FROM python:2
MAINTAINER Alexandre Busquets <abusquets@gmail.com>

RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
    protobuf-compiler \
    libprotobuf-dev \
    libtokyocabinet-dev \
    libgeos-c1v5 \
    libgdal-dev \
    libspatialindex-dev

RUN pip install imposm rtree Shapely==1.5.9

RUN mkdir -p /app
WORKDIR /app
