#!/usr/bin/env bash


for filename in inputfiles/*; do
    python3 ./main.py "$filename"
done
