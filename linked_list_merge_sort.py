from linked_list import LinkedList
from node import Node

linkedlist = LinkedList()


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists contaning a single node
    -Repetedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half,right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_sort(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists.
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2


merge_sort([1,2,3])