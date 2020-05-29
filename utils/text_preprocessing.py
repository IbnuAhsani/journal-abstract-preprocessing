import nltk
import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


stop_word_factory = StopWordRemoverFactory()
stemmer_factory = StemmerFactory()
stopword = stop_word_factory.create_stop_word_remover()
stemmer = stemmer_factory.create_stemmer()


def generate_tokens(abstract):

    abstract_lower_case = abstract.lower()
    abstract_white_spaces_removed = abstract_lower_case.strip()
    abstract_numbers_removed = abstract_white_spaces_removed.translate(string.digits)
    abstract_punctuation_removed = abstract_numbers_removed.translate(string.punctuation)
    abstract_stopword_removed = stopword.remove(
        abstract_punctuation_removed)
    abstract_stemmed = stemmer.stem(abstract_stopword_removed)
    abstract_tokens = nltk.word_tokenize(abstract_stemmed)

    final_token = []

    for token in abstract_tokens:
      token_digits_removed = ''.join([i for i in token if not i.isdigit()])
      final_token.append(token_digits_removed)

    return final_token