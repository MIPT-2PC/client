import json


class ConfigUploader:

    def __init__(self, path=None):
        if path is None:
            raise Exception('No path specified for config.txt file', path)

        dict1 = {}
        # fields in the sample file
        fields = ['inn', 'out', 'inList', 'outList', 'operation']

        with open(path) as file:
            numOfNodes, numOfLinks = file.readline().split()
            AinputBitness, BinputBitness, resultBitness = file.readline().split()
            numerator = 1

            for line in file:

                struct = list(line.strip().split(None, maxsplit=6))

                inNum = int(struct[0])
                outNum = int(struct[1])
                operation = struct[-1]

                dict2 = {}
                inList = []
                outList = []

                for index in range(inNum):
                    inList.append(struct[2 + index])

                for index in range(outNum):
                    outList.append(struct[2 + inNum + index])

                dict2[fields[0]] = inNum
                dict2[fields[1]] = outNum
                dict2[fields[2]] = inList
                dict2[fields[3]] = outList
                dict2[fields[4]] = operation

                namer = 'node' + str(numerator)
                dict1['config'] = {
                    "numOfLinks": numOfLinks,
                    "numOfNodes": numOfNodes,
                    "AinputBitness": AinputBitness,
                    "BinputBitness": BinputBitness,
                    "resultBitness": resultBitness
                }
                dict1[namer] = dict2
                numerator = numerator + 1

        self.dataToTransfer = dict1
