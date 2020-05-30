import nltk
import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


stop_word_factory = StopWordRemoverFactory()
stemmer_factory = StemmerFactory()
stopword = stop_word_factory.create_stop_word_remover()
stemmer = stemmer_factory.create_stemmer()


def generate_tokens(abstract):

    remove_digits = str.maketrans(string.digits, ' '*len(string.digits))
    remove_punctuations = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    abstract_lower_case = abstract.lower()
    abstract_white_spaces_removed = abstract_lower_case.strip()
    abstract_numbers_removed =  abstract_white_spaces_removed.translate(remove_digits)
    abstract_punctuation_removed = abstract_numbers_removed.translate(remove_punctuations)
    abstract_stopword_removed = stopword.remove(
        abstract_punctuation_removed)
    abstract_stemmed = stemmer.stem(abstract_stopword_removed)
    abstract_tokens = nltk.word_tokenize(abstract_stemmed)

    final_abstract_tokens = [token for token in abstract_tokens if len(token) >= 3]

    return final_abstract_tokens