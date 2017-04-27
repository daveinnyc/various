#!/usr/bin/env bash 

###
### Run a simple spider with wget and parse the output for HTML error codes
###
### Copyright 2017, MIT license
###
### DEFAULT: robots.txt file is ignored
### DEFAULT: 1 second wait between requests to avoid hammering site

SITE_URL="some.site.com"         #URL HERE
SITE_TYPE="http://"              #http or https
RUN_TIME=$(date +'%Y-%m-%d..%H%M%S')
OUT_FILE="spider..${SITE_URL}..${RUN_TIME}"
HTTP_CODES="300 301 302 400 401 404 500 501" 

echo "SITE NAME: ${SITE_URL}"
echo

wget  --spider \
      -e robots=off \
      --wait 1 \
      --page-requisites \
      --show-progress \
      --progress=bar:force \
      --recursive \
      --no-parent \
      --output-file=${OUT_FILE} \
      --rejected-log=${OUT_FILE}.rejected \
      ${SITE_TYPE}${SITE_URL} 

for HTTP_CODE in ${HTTP_CODES}
     do  echo 
         echo 
         echo "EROR CODE: ${HTTP_CODE}" 
         grep -B2 " ${HTTP_CODE} " ${OUT_FILE}
     done
