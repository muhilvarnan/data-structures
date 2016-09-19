def printArrayList(arrayList):
    """
    print array list
    """
    for item in arrayList: print item

def getKeyPosition(maxkeyValue):
    """
    Get key Position
    """
    print "Enter position to be inserted"
    key = int(input())
    if key < maxkeyValue:
        return key
    else:
        return getKeyPosition(maxkeyValue)

def main():
    """
    Main function
    """
    arrayList = [1, 2, 3, 4, 5]
    arrayLength = len(arrayList)
    j = arrayLength - 1
    print "Array before insert"
    printArrayList(arrayList)
    key = getKeyPosition(arrayLength)
    print "Enter value to be inserted"
    value = int(input())
    while(j >= key):
        if (j+1) >= arrayLength:
            arrayList.append(arrayList[j])
        else:
            arrayList[j+1] = arrayList[j]
        j = j - 1
    arrayList[key] = value
    print "Array after insert"
    printArrayList(arrayList)

if __name__ =="__main__":
    main()
