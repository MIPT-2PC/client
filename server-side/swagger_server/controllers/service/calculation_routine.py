from threading import Thread
import time
import swagger_client

from swagger_client.rest import ApiException
from pprint import pprint
from queue import Queue
import os

class CalculationRoutine:

    maskedInputNeighbour = None
    maskedInputSelf = None

    result = 0
    globalLinks = [None]

    list = []
    iterator = 0

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

    def gateLogicIndex(self, c, d):
        if c == 0 and d == 0:
            return "0"
        if c == 0 and d == 1:
            return "1"
        if c == 1 and d == 0:
            return "2"
        if c == 1 and d == 1:
            return "3"

    def calculator(self, response):
        print("CALCULATOR STARTED")
        print(response['config'])
        print(response['resultBitness'])

        self.globalLinks = [None] * int(response['config'].numOfLinks)

        print("filling globalLinks with input")

        if os.getenv('CLIENT_A', None) is not None:
            for i in range(int(response['config'].masksBitness)):
                self.globalLinks[i] = self.maskedInputSelf >> i & 1
                self.globalLinks[i + int(response['config'].masksBitness)] = self.maskedInputNeighbour >> i & 1
        if os.getenv('CLIENT_B', None) is not None:
            for i in range(int(response['config'].masksBitness)):
                self.globalLinks[i] = self.maskedInputNeighbour >> i & 1
                self.globalLinks[i + int(response['config'].masksBitness)] = self.maskedInputSelf >> i & 1
        print(self.globalLinks)

        while self.globalLinks.count(None):
            self.iterator += 1
            answerDict = {}
            for k in range(int(response['config'].numOfNodes)):

                node = response['nodes'][k]

                if len(node.inList) == 2:
                    if (self.globalLinks[int(node.inList[0])] is not None) and (self.globalLinks[int(node.inList[1])] is not None) and (self.globalLinks[int(node.outList[0])] is None):
                        logicUnitCell = self.gateLogicIndex(self.globalLinks[int(node.inList[0])], self.globalLinks[int(node.inList[1])])
                        answerDict[int(node.outList[0])] = int(node.operation[int(logicUnitCell)])

                if len(node.inList) == 1:
                    if (self.globalLinks[int(node.inList[0])] is not None) and (self.globalLinks[int(node.outList[0])] is None):
                        logicUnitCell = self.gateLogicIndex(self.globalLinks[int(node.inList[0])], self.globalLinks[int(node.inList[0])])
                        if int(logicUnitCell) == 1 or int(logicUnitCell) == 2:
                            print("BITCH ASS")
                        answerDict[int(node.outList[0])] = int(node.operation[int(logicUnitCell)])
            self.answer.put(answerDict)

            api_instance = swagger_client.InteractionApi()
            body = swagger_client.ExchangePayload(start_index=0, filled_links=answerDict, end_index=0)
            try:
                api_response = api_instance.exchange_out(body=body)
                #self.q.put(api_response[0].filled_links)
                #print(api_response)
            except ApiException as e:
                print("Exception when calling ExternalCallsApi->get_result: %s\n" % e)

            neighbourDict = self.q.get()

            #print("filling global links with xoring answerDict and neighbourDict by the same keys")
            for key in neighbourDict:
                self.globalLinks[int(key)] = answerDict.get(int(key)) ^ neighbourDict.get(key)
            print("вычисленный первый слой А:")
            print(answerDict)
            print("вычисленный первый слой В:")
            print(neighbourDict)
            print("iterator")
            print(self.iterator)

        print("YEY! HERE WE GO AGAIN, answer is ready!")

        #print(self.globalLinks)

        # print("output masks")
        #print("{0:b}".format(int(response['config'].outputMasks)))

        reversedMasks = format(int(response['config'].outputMasks), '34b')[::-1]
        #print("reversed output masks")
        #print(reversedMasks)

        stri = ""
        for i in reversed(range(int(response['config'].numOfLinks))):
            if i < int(response['config'].numOfLinks) - int(response['resultBitness']):
                break
            stri = str(self.globalLinks[i]) + stri

        print("answer")
        print(stri)

        out = int(stri, 2)
        print(out)

        reversedAnswer = stri[::-1]

        #print("reversed masks")
        #print(reversedMasks)
        #print("reversed output")
        #print(reversedAnswer)

        A = int(reversedMasks, 2)
        B = int(reversedAnswer, 2)

        answerYopta = A^B

        print("answer is:")
        print(answerYopta)

        self.clearLocalData()

    def clearLocalData(self):
        self.list.append(self.result)

CalculationRoutineInst = CalculationRoutine()