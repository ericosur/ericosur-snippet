#!/bin/bash

# script to download csv format from gspread with curl
# docid is part of google spread sheet URL

# reference from:
# https://stackoverflow.com/questions/33713084/download-link-for-google-spreadsheets-csv-export-with-multiple-sheets
# https://docs.google.com/spreadsheets/d/{key}/gviz/tq?tqx=out:csv&sheet={sheet_name}

DOCID='DOCID_COPY_IT_FROM_GSPREAD_URL'
SHEETID='SHEET1'
BASE_URL="https://docs.google.com/spreadsheets/d/${DOCID}/gviz/tq?tqx=out:csv&sheet=${SHEETID}"
FILE_NAME='driving_data.csv'

echo ${BASE_URL}
curl ${BASE_URL} > ${FILE_NAME}

