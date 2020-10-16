#!/bin/bash

awk -F',' 'BEGIN{FS=",";OFS=","} ($20=="Closed") && ($2 ~ /\/2020/) && ($3 ~ /\/2020/)    {print $2, $3, $9, $20}' nyc_311_limit.csv > 2020_closed_nyc_311.csv 

