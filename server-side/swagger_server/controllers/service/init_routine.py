from __future__ import print_function

import os

import connexion
import swagger_client_pre
import json
from types import SimpleNamespace

from .config_uploader import *
from swagger_client_pre.rest import ApiException
from pprint import pprint

from threading import Thread
from queue import Queue

app = connexion.FlaskApp(__name__)

class InitRoutine:

    def __init__(self, path):
        ConfigUploaderInst = ConfigUploader(path)

        PreprocessorRoutineInst = SendToPreprocessorRoutine()
        PreprocessorRoutineInst.start(ConfigUploaderInst.dataToTransfer)


class SendToPreprocessorRoutine:

    inputNumber = None
    Response_nodes = []
    gotMaskedInput = False
    maskedInputLocal = 0
    maskedInputNeighbour = 0

    if os.getenv('CLIENT_A', None) is not None:
        adversary = True
    if os.getenv('CLIENT_B', None) is not None:
        inputNumber = 94  # клиент B должен иметь свой API, а я его забыл написать(((
        adversary = False

    def __init__(self):
        pass

    def start(self, dataToTransfer=None):

        if not self.adversary:
            api_instance = swagger_client_pre.PreprocessorApi()

            try:
                print("ClientB call get_table from SendToPreprocessorRoutine")
                api_response = api_instance.get_table()
                print("ClientA get preprocessed value successfully")
                self.config = json.loads(json.dumps(api_response[0]['config']), object_hook=lambda d: SimpleNamespace(**d))

                self.numOfLinks = int(self.config.numOfLinks)  # количество линков в цепи (конфиге)
                self.numOfNodes = int(self.config.numOfNodes)  # количество узлов в цепи (конфиге)
                self.masksBitness = int(self.config.masksBitness)  # количество бит клиента А
                self.inputMasks = int(self.config.inputMasks)  # количество бит клиента B
                self.outputMasks = int(self.config.outputMasks)  # количество бит результата

                self.nodes = [0] * self.numOfNodes

                for i in range(self.numOfNodes):
                    self.nodes[i] = json.loads(json.dumps(api_response[0]['node' + str(i + 1)]), object_hook=lambda d: SimpleNamespace(**d))
                print("ClientA parsed preprocessed data successfully")

            except ApiException as e:
                print("Exception when calling InteractionApi->get_table: %s\n" % e)

        if self.adversary:
            api_instance = swagger_client_pre.PreprocessorApi()

            try:
                # start preprocessing procedure
                print("ClientA send start_2pc post request to preprocessor")
                api_response = api_instance.start2_pc(body=dataToTransfer)
                print("ClientA get preprocessed value successfully")
                self.config = json.loads(json.dumps(api_response[0]['config']), object_hook=lambda d: SimpleNamespace(**d))

                self.numOfLinks = int(self.config.numOfLinks)  # количество линков в цепи (конфиге)
                self.numOfNodes = int(self.config.numOfNodes)  # количество узлов в цепи (конфиге)
                self.masksBitness = int(self.config.masksBitness)  # битность маски
                self.inputMasks = int(self.config.inputMasks)  # маскируюшие биты входа
                self.outputMasks = int(self.config.outputMasks)  # маскируюшие биты выхода

                self.nodes = [0] * self.numOfNodes

                for i in range(self.numOfNodes):
                    self.nodes[i] = json.loads(json.dumps(api_response[0]['node' + str(i + 1)]), object_hook=lambda d: SimpleNamespace(**d))
                print("ClientA parsed preprocessed data successfully")

                print(api_response)
            except ApiException as e:
                print("Exception when calling InteractionApi->start2_pc: %s\n" % e)

SendToPreprocessorRoutineInst = SendToPreprocessorRoutine()