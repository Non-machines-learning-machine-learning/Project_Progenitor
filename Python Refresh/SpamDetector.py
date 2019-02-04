import os
import glob
from FunctionTimerCode import time_func
from nltk.corpus import names
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

all_names = set(names.words())

def get_text_files(file_path, encoding='UTF-8'):
    """Return list of all text files in path"""
    file_list = []
    for filename in glob.iglob(os.path.join(file_path, '*.txt')):
        with open(filename, 'r', encoding=encoding) as infile:
            file_list.append(infile.read())
    return file_list

def letter_only(astr):
    return astr.isalpha()

def person_name(astr):
    return astr in names.words()

def stem_word(word):
    """Reduces word to stem, base or root form."""
    porter_stemmer = PorterStemmer()
    return porter_stemmer.stem(word)

def clean_doc(text_doc):
    """Return simplifed text_doc with:
        - All lower
        - All alphabetical
        - Word stemmed"""
    return ' '.join([stem_word(word.lower()) 
                for word in text_doc.split()
                if letter_only(word)
                and word not in all_names])


path1 = '/Users/DC/Desktop/Python Machine Learning/Python Machine Learning by Example/enron1/spam/'
path2 = '/Users/DC/Desktop/Python Machine Learning/Python Machine Learning by Example/enron1/ham/'
spam_emails = [clean_doc(doc) for doc in get_text_files(path1, 'ISO-8859-1')[0:50]] #limited set of emails for testing
ham_emails = [clean_doc(doc) for doc in get_text_files(path2, 'ISO-8859-1')[0:50]] #limited set of emails for testing
vectorizer = CountVectorizer(stop_words="english", max_features=500)
vectorizer.fit(spam_emails + ham_emails)
term_spam_emails = vectorizer.transform(spam_emails)
term_ham_emails = vectorizer.transform(ham_emails)


print(vectorizer.get_feature_names())
print(term_ham_emails.toarray())

