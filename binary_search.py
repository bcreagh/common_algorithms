#An implementation of a binary search function

#Searches an ORDERED list of numeric values for a target value
#If found, returns the index of the target
#If not, it returns -1

#Worst case: O(log n)
#Average case: O(log n)


def binSearch(myList, target):
    totalElements = len(myList)
    min = 0
    max = totalElements - 1
    
    while min <= max:
        middleElement = min + int((max - min) // 2)
        if myList[middleElement] == target:
            return middleElement
        elif myList[middleElement] > target:
            max = middleElement - 1
        else:
            min = middleElement + 1
    
    return -1
            
     