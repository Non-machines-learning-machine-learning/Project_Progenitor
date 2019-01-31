import os
import glob
from functools import reduce
from nltk.corpus import names
from FunctionTimerCode import time_func
from nltk.stem import WordNetLemmatizer

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
    return astr in names.words()

path1 = '/Users/DC/Desktop/Python Machine Learning/Python Machine Learning by Example/enron1/spam/'
path2 = '/Users/DC/Desktop/Python Machine Learning/Python Machine Learning by Example/enron1/ham/'
spam_emails = get_text_files(path1, 'ISO-8859-1')
ham_emails = get_text_files(path2, 'ISO-8859-1')
all_names = set(names.words()) # Set of common names for reference.


def stem(text_doc):
    """Reduces each word in the text documment to their word stem, base or root form."""
    lemmatizer = WordNetLemmatizer() 
    # Stemmers remove morphological affixes from words, leaving only the word stem.
    return ' '.join([lemmatizer.lemmatize(word.lower()) for word in text_doc.split()])


