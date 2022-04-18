#!/bin/bash

stmatch\
 --network  ../maryland-latest.osm.pbf
 --gps_file master_log.csv\
 --gps_x jetson_rpi_lng\
 --gps_y jetson_rpi_lat\
 --gps_timestamp timestamp\
 --gps_id Id\
 -k 16 -r 0.005 -e 0.0005\
 --vmax 0.0002\
 --output maryland_match.txt