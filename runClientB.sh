cd client-of-preprocessor/ || exit
pip3 install -r requirements.txt
python3 setup.py install

cd ../client-side/ || exit
pip3 install -r requirements.txt
python3 setup.py install

cd ../server-side/ || exit
pip3 install -r requirements.txt
python3 setup.py install

export CLIENT_B_NUMBER=94
export CLIENT_B=8081
export NEIGHBOR_PORT=8080
python3 -m swagger_server