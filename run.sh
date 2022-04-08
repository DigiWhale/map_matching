#!/bin/bash

fmm --ubodt ubodt_config.txt\
 --network maryland/edges.shp\
 --network_id fid\
 --source u\
 --target v\
 --gps ../road_network/master_log.csv\
 --gps_point -k 4 -r 0.4 -e 0.5\
 --output mr.csv\
 --output_fields all\
 --gps_x jetson_rpi_lng\
 --gps_y jetson_rpi_lat\
 --gps_timestamp timestamp\
 --gps_id Id\
