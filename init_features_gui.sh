#!/bin/sh
serf-makemigrations
serf-migrate

python import_batch.py
echo Initialization Complete!
echo Copy and paste the following line to start the GUI
echo python features_gui.py
