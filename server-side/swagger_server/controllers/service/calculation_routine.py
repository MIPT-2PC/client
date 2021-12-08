from threading import Thread
import time
import swagger_client

from swagger_client.rest import ApiException
from pprint import pprint
from queue import Queue
import os

class CalculationRoutine:

    layer = 0
    result = [None] * 16
    position = 7
    list = []
    neighbour = 0

    def __init__(self):
        self.q = Queue()
        self.answer = Queue()

        self.q.put((7, 1))
        for i in range(8):
            self.result[i] = 255 >> i & 1

    def start(self, response):
        if os.getenv('CLIENT_A', None) is not None:
            print("ClientA start() function is called, creating new thread")
        if os.getenv('CLIENT_B', None) is not None:
            print("ClientB start() function is called, creating new thread")
        t1 = Thread(target=self.calculator(response), args=(self.q,))
        t1.start()

    def calculator(self, response):
        print("CALCULATOR STARTED")
        print(response)

        while True:
            print("[position=" + str(self.position) + "]")
            self.result[self.position] = 1
            if self.position != 15:
                self.position += 1
            self.answer.put((self.position, 1))

            api_instance = swagger_client.InteractionApi()
            body = swagger_client.ExchangePayload(start_index=self.position, out_dec_number=1)
            try:
                api_response = api_instance.exchange_out(body=body)
                self.q.put((api_response[0].start_index, api_response[0].out_dec_number))
                print(api_response)
            except ApiException as e:
                print("Exception when calling ExternalCallsApi->get_result: %s\n" % e)
            self.neighbour, kek = self.q.get()
            print("Neighbour value: " + str(self.neighbour))

            if self.position == 15 and self.neighbour == 15:
                break
        print("YEY! HERE WE GO AGAIN, answer is ready!")
        print(self.result)
        self.list.append(self.result)
        self.layer = 0
        self.position = 7
        self.result = [None] * 16
        self.q = Queue()
        self.answer = Queue()
        self.neighbour = 7

CalculationRoutineInst = CalculationRoutine()