import json
import nltk
import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


with open('./data/stop-words.json') as f:
    reference_stopword_arr = json.load(f)

reference_stopword_dict = ArrayDictionary(reference_stopword_arr)
stopword_remover = StopWordRemover(reference_stopword_dict)
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()


def generate_tokens(abstract):

    remove_digits = str.maketrans(string.digits, ' '*len(string.digits))
    remove_punctuations = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    abstract_lower_case = abstract.lower()
    abstract_white_spaces_removed = abstract_lower_case.strip()
    abstract_numbers_removed =  abstract_white_spaces_removed.translate(remove_digits)
    abstract_punctuation_removed = abstract_numbers_removed.translate(remove_punctuations)
    abstract_stopword_removed = stopword_remover.remove(abstract_punctuation_removed)
    abstract_stemmed = stemmer.stem(abstract_stopword_removed)
    abstract_tokens = nltk.word_tokenize(abstract_stemmed)

    final_abstract_tokens = [token for token in abstract_tokens if len(token) >= 3]

    return final_abstract_tokens