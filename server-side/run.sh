cd ../client-of-preprocessor || exit
pip3 install -r requirements.txt
python3 setup.py install

cd ../client-side || exit
pip3 install -r requirements.txt
python3 setup.py install

cd ../server-side || exit
pip3 install -r requirements.txt
python3 setup.py install
python3 -m swagger_server