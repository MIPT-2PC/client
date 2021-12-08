#!/usr/bin/env python3
# patched by ProValdi

import connexion
import os

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'User exchange API'}, pythonic_params=True)
    if os.getenv('CLIENT_A', None) is not None:
        cliPort = os.getenv('CLIENT_A', None)
    if os.getenv('CLIENT_B', None) is not None:
        cliPort = os.getenv('CLIENT_B', None)
    app.run(port=int(cliPort))


if __name__ == '__main__':
    main()
