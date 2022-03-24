#!/bin/bash

# Modify URL before using and update metadata in config.py
mkdir -p ../HGNC
wget -O ../HGNC/hgnc_complete_set.txt  http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/archive/monthly/tsv/hgnc_complete_set_2022-03-01.txt
