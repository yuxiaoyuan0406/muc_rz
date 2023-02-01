#!/bin/bash
sudo cp rz/ /etc/ -r
sudo cp rz.py /etc/rz/
sudo cp rz.service /usr/lib/systemd/system/

sudo cp *.json /etc/rz/

# sudo systemctl enable rz
