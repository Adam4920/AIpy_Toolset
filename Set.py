class set:
    def __init__(self, name, data):
        self.name = name
        self.data = data


def createFromFile(fileName):
    file = open(fileName, "r")
    lines = []

    for line in file:
        lines.append(line.rstrip().split(";"))

    y = len(lines[0]) - 1

    dataName = [lines[0][0]]
    yData = [lines[0][y]]
    xData = []

    for i in range(1, len(lines)):
        dataName.append(lines[i][0])
        yData.append(lines[i][y])

    for z in range(1, y):
        t = []
        for i in range(0, len(lines)):
            t.append(lines[i][z])
        xData.append(t)

    temp = []
    for i in range(1, len(dataName)):
        temp.append(dataName[i])
    identifiers = set(dataName[0], temp)

    temp = []
    for i in range(1, len(yData)):
        temp.append(yData[i])
    yResults = set(yData[0], temp)

    xResults = []
    for i in range(0, len(xData)):
        temp = []
        for z in range(1, len(xData[0])):
            temp.append(xData[i][z])
        xResults.append(set(xData[0][i], temp))

    return [identifiers, xResults, yResults]
