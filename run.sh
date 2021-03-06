#!/bin/bash

fmm --ubodt ubodt_config.txt\
 --network maryland/edges.shp\
 --network_id fid\
 --source u\
 --target v\
 --gps ../road_network/master_log.csv\
 --gps_point -k 8 -r 3 -e 800\
 --output output.csv\
 --output_fields all\
 --gps_x jetson_rpi_lng\
 --gps_y jetson_rpi_lat\
 --gps_timestamp timestamp\
 --gps_id Id\
 --use_omp\
