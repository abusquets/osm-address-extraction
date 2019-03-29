#!/bin/bash

docker run --rm -v ${PWD}:/app -ti address-extraction-osm /bin/bash -c "python parse_osm.py $@"
