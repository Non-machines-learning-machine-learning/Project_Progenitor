from timeit import default_timer as timer
from math import ceil, floor
import time
from functools import reduce

def time_func(func, *args, iterat=100):
    "Average run time of a function"
    times = []
    for _ in range(iterat):
            start_time = timer()
            func(*args)
            times.append(timer() - start_time)
    return str(func) + ' average run time of ' + sig_figures(get_average(times),3) + ' and deviation of ' + sig_figures(get_deviation(times),3)

def dec_places(num, places):
     """Returns number in truncated string format limited to decimal places"""
     assert type(num) is float, "num is not a float."
     assert type(places) is int, "places is not an integer."
     decimal_places = len(repr(num)) - len(repr(floor(num))) - 1
     places = min(decimal_places, places)
     for i in range(len(repr(floor(num)))+1, len(repr(num))):
         if repr(num)[i] == '0':
             places += 1
         else:
             break
     places = min(places, decimal_places)
     num_out = str(floor(num)) + '.'
     for i in range(len(num_out), len(num_out) + places):
         num_out += repr(num)[i]
     if len(num_out) == len(repr(floor(num))) +1:
         num_out += '0'
     return num_out


def sig_figures(num, places):
    """Returns number in truncated string format limited to significant figures"""
    assert type(num) is float, "num is not a float."
    assert type(places) is int, "places is not an integer."
    num_out = ''
    # add whole digits
    for i in range(min(len(repr(floor(num))), places)):
        num_out += repr(num)[i]
    # add whole trailing zeros
    for i in range(max(0, len(repr(floor(num))) - places)):
        num_out += '0'
    # add decimal places
    if len(repr(floor(num))) > places:
        num_out += '.0'
    else:
        num_out = dec_places(num, places - len(repr(floor(num))))
    return num_out


def get_average(num_list):
    """Return float average of number list"""
    try:
        return reduce(lambda x, y: x + y, num_list) / len(num_list)
    except:
        raise ValueError("Invalid type entered")


def get_deviation(num_list):
    """Return the float deviation of number list"""
    average = get_average(num_list)
    try:
        return (sum((average - value) ** 2 for value in num_list) / len(num_list)) ** 0.5
    except:
        raise ValueError("Invalid type entered")


def binary_search(alist, item):
    "Using binary search algorithm to search a sorted list"
    search_start = 0
    search_end = len(alist) - 1 
    while True:
        midpoint = ceil((search_start + search_end) / 2)
        if alist[midpoint] == item:
            return True
        if search_start == midpoint or search_end == midpoint:
            return False
        if alist[midpoint] > item:
            search_end = midpoint
        else:
            search_start = midpoint

