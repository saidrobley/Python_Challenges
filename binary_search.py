def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        middlepoint = (first + last)//2
        if list[middlepoint] == target:
            return middlepoint
        elif list[middlepoint] < target:
            first = middlepoint + 1
        else:
            last = middlepoint - 1
    return -1
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 11)
verify(result)