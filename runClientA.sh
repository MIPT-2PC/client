#!/bin/bash

cd client-of-preprocessor || exit
pip3 install -r requirements.txt
python3 setup.py install
cd ..
python3 main.py



