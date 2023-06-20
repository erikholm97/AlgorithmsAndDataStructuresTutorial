def merge_sort_list(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Mege the sorted sublists created in previous step

    Takes 0(n log n) time
    """

    if len(list) <= 1:
        return list
    
    left_half,right_half = split(list)
    left = merge_sort_list(left_half)
    right = merge_sort_list(right_half)

    return merge_sort(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right

    Takes overall n(k log n) time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left,right

def merge_sort(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall 0(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j+=1

    #Account for if right list is shorter than right.
    while i < len(left):
        l.append(left[i])
        i+=1

    #Account for if right list is shorter than right.
    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    n = len(list)

    if n== 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54,62,93,17,77,31,44,55,20]
l = merge_sort_list(alist)

print(verify_sorted(alist))
print(verify_sorted(l))