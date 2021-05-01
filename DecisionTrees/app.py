from Set import set, createFromFile

print("Please enter your data in 'data.csv'. [Enter] to continue...")
input()

# retrieve data
identifiers, xList, yData = createFromFile("data.csv")


print("Enter the starting point of the data to train: (e.g: 1)")
tStart = int(input())

print("Enter the end point of the data to train: (e.g: 10)")
tEnd = int(input())
