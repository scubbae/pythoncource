myUniqueList = []
myLeftovers = []


def addToList(add):
    # this is "if" statement assume "Car" is already in the.
    if add == "Car":
        myUniqueList.append(False)
        myLeftovers.append(add)
    else:
        myUniqueList.append(True)


addToList("Car")
addToList("Truck")
addToList("Van")
addToList("Bike")

print("Approve List")
print(myUniqueList)


print("Reject List")
print(myLeftovers)
