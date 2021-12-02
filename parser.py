# Python program to convert text
# file to JSON


import json

# the file to be converted
filename = 'config.txt'


# algorithm to convert our config.txt to config.json
'''
# resultant dictionary
dict1 = {}

# fields in the sample file
fields = ['in', 'out', 'inList', 'outList', 'operation']

with open(filename) as file:
    numOfNodes, numOfLinks = file.readline().split()
    NA, NB, NOUT = file.readline().split()

    # count variable for employee id creation
    l = 1

    for line in file:

        # reading line by line from the text file
        struct = list(line.strip().split(None, maxsplit=6))

        # for output see below
        print(struct)

        # for automatic creation of id for each employee
        sno = 'node' + str(l)

        # intermediate dictionary
        dict2 = {}
        inList = []
        outList = []

        for index in range(int(struct[0])):
            inList.append(struct[2 + index])

        for index in range(int(struct[1])):
            outList.append(struct[2 + int(struct[0]) + index])

        dict2[fields[0]] = struct[0]
        dict2[fields[1]] = struct[1]
        dict2[fields[2]] = inList
        dict2[fields[3]] = outList
        dict2[fields[4]] = struct[-1]

        # appending the record of each node to
        # the main dictionary
        dict1[sno] = dict2
        l = l + 1

# creating json file
out_file = open("test2.json", "w")
json.dump(dict1, out_file, indent=4)
out_file.close()
'''