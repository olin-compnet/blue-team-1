#!/bin/bash
cd ~/compnet
scp -r * pi@172.18.0.22:~/compnet
scp -r * pi@172.18.0.26:~/compnet
scp -r * pi@172.18.0.33:~/deploy

