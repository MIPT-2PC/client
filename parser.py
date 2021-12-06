# Python program to convert text
# file to JSON


import json
from types import SimpleNamespace
import operator

# the file to be converted
filename = 'config.txt'

dict1 = {}

# fields in the sample file
fields = ['inn', 'out', 'inList', 'outList', 'operation', 'used']

operations = {
    "XOR": lambda x, y: x ^ y,
    "AND": lambda x, y: x & y,
    "INV": lambda x: 1 if x == 0 else 0
}

with open(filename) as file:
    numOfNodes, numOfLinks = file.readline().split()
    NA, NB, NOUT = file.readline().split()
    inputA, inputB = file.readline().split()

    l = 1

    for line in file:

        # reading line by line from the text file
        struct = list(line.strip().split(None, maxsplit=6))

        # intermediate dictionary

        InNum = int(struct[0])
        OutNum = int(struct[1])
        operation = struct[-1]

        sno = 'node' + str(l)

        # intermediate dictionary
        dict2 = {}
        inList = []
        outList = []

        for index in range(int(struct[0])):
            inList.append(struct[2 + index])

        for index in range(int(struct[1])):
            outList.append(struct[2 + int(struct[0]) + index])

        dict2[fields[0]] = int(struct[0])
        dict2[fields[1]] = int(struct[1])
        dict2[fields[2]] = inList
        dict2[fields[3]] = outList
        dict2[fields[4]] = struct[-1]
        dict2[fields[5]] = False

        # appending the record of each node to
        # the main dictionary
        dict1[sno] = dict2
        l = l + 1

out_file = open("config.json", "w")
json.dump(dict1, out_file, indent=4)
data = json.dumps(dict1)
out_file.close()

links = [None] * int(numOfLinks)

for i in range(int(NA)):
    links[i] = int(inputA) >> i & 1
    links[i+32] = int(inputB) >> i & 1

nodes = [0] * int(numOfNodes)

for i in range(int(numOfNodes)):
    nodes[i] = json.loads(json.dumps(dict1['node'+ str(i + 1)]), object_hook=lambda d: SimpleNamespace(**d))

print(nodes[0].inList[1])

i = 0

while links.count(None):
    if not nodes[i].inList.count(None):
        if len(nodes[i].inList) == 1:
            links[int(nodes[i].outList[0])] = operations[nodes[i].operation](links[int(nodes[i].inList[0])])
        if len(nodes[i].inList) == 2:
            links[int(nodes[i].outList[0])] = operations[nodes[i].operation](links[int(nodes[i].inList[0])], links[int(nodes[i].inList[1])])
    i = i + 1 # т.к. config отсортирован, то это подойдёт, но на самом деле надо каждый раз заново пробегать по всем узлам
    # или есть поменять в конфиге пару строчек местами, то считать уже будет неправильно

out = 0
stri = ""

print(links)

for i in reversed(range(int(numOfLinks))):
    if i < int(numOfLinks) - int(NOUT):
        break
    out = out << links[i] | 1
    stri = stri + str(links[i])

print(int(stri, 2))