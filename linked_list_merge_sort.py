from linked_list import LinkedList
from linked_list import Node

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists contaning a single node
    -Repetedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    