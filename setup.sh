#!/bin/sh

# Data folder
export DATA_FOLDER="data"

# Data url
DATA_URL="https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"
mkdir $DATA_FOLDER

# Install required python libraries
pip install -r requirements.txt

# Download data
echo "Downloading Wikipedia articles dump.."
curl -sS $DATA_URL > "$DATA_FOLDER/enwiki-latest-pages-articles.xml.bz2"

# Run python script from training the model
python train.py

# Evaluate the model
python test.py
