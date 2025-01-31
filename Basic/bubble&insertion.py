import random
import time

def bubbleSort(aList):
    for i in range(len(aList)):
        switched = False
        for j in range(len(aList) - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]
                switched = True
        if not switched:
            break
    return aList


def insertionSort(aList):
    for i in range(1, len(aList)):
        if aList[i] < aList[i - 1]:
            for j in range(i, 0, -1):
                if aList[j] < aList[j - 1]:
                    aList[j], aList[j - 1] = aList[j - 1], aList[j]
                else:
                    break
    return aList

nums = [random.randint(0, 100) for i in range(5000)]
start = time.time()
bubbleSort(nums)
print(time.time() - start)

start = time.time()
insertionSort(nums)
print(time.time() - start)