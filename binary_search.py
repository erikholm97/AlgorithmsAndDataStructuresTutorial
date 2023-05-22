def binary_search(list, target): 
    first = 0 #Define the first number.
    last = len(list) - 1 #Define the last number.

    while first <= last:
        midpoint = (first + last)//2 #Rounds down to nearest whole number. For example 7 / 3 = 3 (Instead of 3.5)

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1 #First number will be set to mid point + 1.
        else:
            last = midpoint - 1 #Last number will be set to mid point - 1.

    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)

verify(result)

result = binary_search(numbers, 6)

verify(result)
        

