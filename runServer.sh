#!/bin/bash

sudo hciconfig hci0 up
sudo hciconfig hci0 piscan
python3 rfcomm-serverpy3.py