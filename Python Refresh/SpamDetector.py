import os
import glob
from functools import reduce
from nltk.corpus import names
import FunctionTimerCode

def get_text_files(file_path, encoding='UTF-8'):
    """Return list of all text files in path"""
    file_list = []
    for filename in glob.iglob(os.path.join(file_path, '*.txt')):
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

# print(time_func(is_person_name3, 'Daniel'))


# path1 = 'enron1/spam/'
# path2 = 'enron1/ham/'
# encoding = 'ISO-8859-1'
# spam_emails = get_text_files(path1, encoding)
# ham_emails = get_text_files(path2, encoding)


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