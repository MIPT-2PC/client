cd client-of-preprocessor/ || exit
pip3 install -r requirements.txt
python setup.py install

cd ../client-side/ || exit
pip3 install -r requirements.txt
python setup.py install

cd ../server-side/ || exit
pip3 install -r requirements.txt
python setup.py install

export CLIENT_B=8081
export NEIGHBOR_PORT=8080
python -m swagger_server