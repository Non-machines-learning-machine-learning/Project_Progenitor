from math import floor


def binary_search(alist, item):
    "Using binary search algorithm to search a sorted list"
    search_start = 0
    search_end = len(alist) - 1 
    if search_start > search_end:
        return False
    midpoint = floor((search_start + search_end) / 2)
    if alist[midpoint] < item:
        search_start = midpoint + 1
    elif alist[midpoint] > item:
        search_end = midpoint - 1
    if alist[midpoint] == item:
        return True