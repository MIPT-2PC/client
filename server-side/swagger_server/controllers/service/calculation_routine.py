from threading import Thread
import time
import swagger_client

from swagger_client.rest import ApiException
from pprint import pprint
from queue import Queue

class CalculationRoutine:

    layer = 0
    result = [None] * 16
    position = 0

    def __init__(self):
        self.q = Queue()
        self.answer = Queue()

        self.q.put((0, 1))
        for i in range(8):
            self.result[i] = 1 >> i & 1

    def start(self, response):
        t1 = Thread(target=self.calculator(response), args=(self.q,))
        t1.daemon = True
        t1.start()

    def calculator(self, response):
        print("CALCULATOR STARTED")
        print(response)

        while self.result.count(None):
            self.position, kek = self.q.get()
            self.result[self.position] = 1
            self.position += 1
            self.answer.put(self.position, kek)

            api_instance = swagger_client.InteractionApi()
            body = swagger_client.ExchangePayload(start_index=self.position, out_dec_number=self.result)
            try:
                api_response = api_instance.exchange_out(body=body)
                self.q.put((api_response[0].start_index, api_response[0].out_dec_number))
                print(api_response)
            except ApiException as e:
                print("Exception when calling ExternalCallsApi->get_result: %s\n" % e)

CalculationRoutineInst = CalculationRoutine()