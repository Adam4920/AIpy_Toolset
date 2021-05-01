from Set import set, createFromFile
from Instructions import instructions

print("Please enter your data in 'data.csv'. [Enter] to continue...")
input()

# retrieve data
identifiers, xList, yData = createFromFile("data.csv")

print("Enter the starting point of the data to train: (e.g: 1)")
tStart = int(input())

print("Enter the end point of the data to train: (e.g: 10)")
tEnd = int(input())

instr = instructions([tStart, tEnd])

rawI = identifiers.data[tStart-1:tEnd]
rawXList = xList[tStart-1:tEnd]
rawY = yData.data[tStart-1:tEnd]
