import os
from operator import itemgetter
from utils import input_output as io
from langdetect import detect


DATASET_DIR = "./data/input/dataset-sample.csv"
SAVE_PATH = "./data/output/data-sample-english-sentence-removed.csv"


def main():
    csv_data_list = io.read_csv(DATASET_DIR)
    article_list = []

    csv_header = ['JOURNAL_TITLE', 'ARTICLE_TITLE', 'ARTICLE_ABSTRACT']

    article_list.append(csv_header)

    for i in range(len(csv_data_list)):
        row = csv_data_list[i]

        journal_title, article_title, article_abstract = itemgetter(
            'JOURNAL_TITLE', 'ARTICLE_TITLE', 'ARTICLE_ABSTRACT')(row)

        if article_abstract[-1] != '.':
            article_abstract += '.'

        article_abstract_sentences = article_abstract.split('.')

        j = 0
        article_english_sentence_removed = ''

        while article_abstract_sentences[j]:
            article_sentence = article_abstract_sentences[j]

            try:
                article_sentence_language = detect(article_sentence)
            except:
                article_sentence_language = 'error'

            if(article_sentence_language == 'en'):
                article_abstract_sentences.remove(article_sentence)
                continue

            article_english_sentence_removed += article_sentence + '. '
            j += 1

        article = [journal_title, article_title, article_english_sentence_removed]

        article_list.append(article)

    io.save_articles_csv(SAVE_PATH, article_list)


if __name__ == '__main__':
    main()
