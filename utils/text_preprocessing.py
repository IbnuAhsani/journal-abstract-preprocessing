import json
import nltk
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def generate_tokens(abstract):

    with open('./data/stop-words.json') as f:
        stop_words = json.load(f)

    stemmer_factory = StemmerFactory()
    stemmer = stemmer_factory.create_stemmer()

    remove_digits = str.maketrans(string.digits, ' '*len(string.digits))
    remove_punctuations = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    abstract_lower_case = abstract.lower()
    abstract_white_spaces_removed = abstract_lower_case.strip()
    abstract_numbers_removed =  abstract_white_spaces_removed.translate(remove_digits)
    abstract_punctuation_removed = abstract_numbers_removed.translate(remove_punctuations)
    abstract_punctuation_removed_list = abstract_punctuation_removed.split()
    abstract_sw_removed_list = [word for word in abstract_punctuation_removed_list if word not in stop_words]
    abstract_sw_removed = " ".join(abstract_sw_removed_list)    
    abstract_stemmed = stemmer.stem(abstract_sw_removed)
    abstract_tokens = nltk.word_tokenize(abstract_stemmed)

    final_abstract_tokens = [token for token in abstract_tokens if len(token) >= 3]

    return final_abstract_tokens