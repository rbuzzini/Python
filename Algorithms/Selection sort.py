# Function to find the index off the biggest index element
def findBiggest(arr):
    biggest = arr[0]
    biggest_index = 0

    for i in range(len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]    
            biggest_index = i
    
    return biggest_index

# This runs in O(n) time

# Selection sort algorithm:
def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        newArr.append(max(arr))
        del arr[findBiggest(arr)]
        # I could use newArr.append(arr.pop(findBiggest(arr)))
    
    return newArr


# This runs in O(n x n) time

l = [1, 5, 10]
print(selectionSort(l))
