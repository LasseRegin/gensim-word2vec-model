#!/bin/sh

# Data folder
export DATA_FOLDER="data"

# Data url
DATA_URL="https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"
mkdir $DATA_FOLDER

# Download data
echo "Downloading Wikipedia articles dump.."
curl -sS $DATA_URL > "$DATA_FOLDER/enwiki-latest-pages-articles.xml.bz2"
