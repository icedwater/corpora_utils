# corpora_utils

This is a collection of tools to wangle corpora into exportable formats like
CSV, and so on. It started with a simple script for generating a CSV file of
collated .txt dialogue transcripts as a .csv, because people Excel when they
are familiar with the software they use.

## Pre-requisites

- Python 3.5.2 (will be made more general later on.)

## Components

- **ldc2csv.py**: takes as command line input a text transcript `file.txt`
                  and outputs `file.csv` where the fields are now 1 column
                  each

