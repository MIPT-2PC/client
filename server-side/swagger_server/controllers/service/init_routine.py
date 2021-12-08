from __future__ import print_function

import os

import connexion
import swagger_client_pre

from .config_uploader import *
from swagger_client_pre.rest import ApiException
from pprint import pprint

app = connexion.FlaskApp(__name__)

class InitRoutine:

    def __init__(self, path):
        ConfigUploaderInst = ConfigUploader(path)

        PreprocessorRoutineInst = SendToPreprocessorRoutine()
        PreprocessorRoutineInst.start(ConfigUploaderInst.dataToTransfer)


class SendToPreprocessorRoutine:

    if os.getenv('CLIENT_A', None) is not None:
        adversary = True
    if os.getenv('CLIENT_B', None) is not None:
        adversary = False

    def __init__(self):
        pass

    def start(self, dataToTransfer=None):

        if not self.adversary:
            api_instance = swagger_client_pre.PreprocessorApi()

            try:
                # hello message to get preprocessed data
                api_response = api_instance.get_table()
                self.ClientB_Response = api_response
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling InteractionApi->get_table: %s\n" % e)

        if self.adversary:
            api_instance = swagger_client_pre.PreprocessorApi()

            try:
                # start preprocessing procedure
                api_response = api_instance.start2_pc(body=dataToTransfer)
                self.ClientA_Response = api_response
                print(api_response[0])
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling InteractionApi->start2_pc: %s\n" % e)
