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

    adversary = True

    def __init__(self):
        pass

    def start(self, dataToTransfer):

        if not self.adversary:
            api_instance = swagger_client_pre.PreprocessorApi()

            try:
                # hello message to get preprocessed data
                api_response = api_instance.get_table()
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling InteractionApi->get_table: %s\n" % e)

        if self.adversary:
            api_instance = swagger_client_pre.PreprocessorApi()

            try:
                # start preprocessing procedure
                api_response = api_instance.start2_pc(body=dataToTransfer)
                print(api_response[0])
                print(api_response[0])
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling InteractionApi->start2_pc: %s\n" % e)
