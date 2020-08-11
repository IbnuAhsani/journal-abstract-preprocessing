import os
import json
from operator import itemgetter
from utils import input_output as io


DATASET_DIR = "./data/input/dataset-sample.csv"
JOINED_WORDS_DIR = "./data/output/joined-words.json"
SAVE_PATH = "./data/output/data-sample-joined-words-removed.csv"


def main():
    csv_data_list = io.read_csv(DATASET_DIR)
    article_list = []

    csv_header = ['JOURNAL_TITLE', 'ARTICLE_TITLE', 'ARTICLE_ABSTRACT']

    article_list.append(csv_header)

    with open(JOINED_WORDS_DIR) as f:
        joined_words = json.load(f)

    for i in range(len(csv_data_list)):
        row = csv_data_list[i]

        journal_title, article_title, article_abstract = itemgetter(
            'JOURNAL_TITLE', 'ARTICLE_TITLE', 'ARTICLE_ABSTRACT')(row)

        if article_abstract[-1] != '.':
            article_abstract += '.'

        article_abstract_words = article_abstract.split()
        article_abstract_joined_words_removed = ''

        for j in range(len(article_abstract_words)):
            word = article_abstract_words[j]
        
            if word in joined_words:
                article_abstract_joined_words_removed += ' ' + joined_words[word]
            else:
                article_abstract_joined_words_removed += ' ' + word

        article = [journal_title, article_title, article_abstract_joined_words_removed]

        article_list.append(article)

    io.save_articles_csv(SAVE_PATH, article_list)


if __name__ == '__main__':
    main()
