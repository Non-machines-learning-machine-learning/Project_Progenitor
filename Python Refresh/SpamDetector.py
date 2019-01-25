import os
import glob
from functools import reduce
from nltk.corpus import names
from timeit import default_timer as timer
from math import ceil

def time_func(func, *args, iterations=1000):
    "Average run time of a function"
    average_times = []
    for _ in range(3):
        times = []
        for _ in range(iterations):
            start_time = timer()
            func(*args)
            times.append(timer() - start_time)
        average_times.append(str(reduce(lambda x, y: x + y, times) / len(times)))
    print(average_times)

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

def get_text_files(file_path, encoding='UTF-8'):
    file_list = []
    for filename in glob.iglob(os.path.join(path1, '*.txt')):
        with open(filename, 'r', encoding=encoding) as infile:
            file_list.append(infile.read())
    return file_list

def is_letter_only(astr):
    return astr.isalpha()

def is_person_name(astr):
    all_names = iter(names.words())
    return astr in all_names

def is_person_name2(astr):
    return astr in names.words()

def is_person_name3(astr):
    return binary_search(names.words(), astr)


# print(time_func(is_person_name, ['Daniel']))

# print(time_func(is_person_name2, ['Daniel']))

print(time_func(is_person_name3, 'Daniel'))


path1 = 'enron1/spam/'
path2 = 'enron1/ham/'
encoding = 'ISO-8859-1'
spam_emails = get_text_files(path1, encoding)
ham_emails = get_text_files(path2, encoding)


# all_names = set(names.words())
# lemmatizer = WordNetLemmatizer()

# def clean_text(docs):
#     cleaned_docs = []
#     for doc in docs:
#         cleaned_docs.append(' '.join([lemmatizer.lemmatize(word.lower())
#             for word in doc.split()
#             if letter_only(word)
#             and word not in all_names]))
#     return cleaned_docs