import os
import json
from operator import itemgetter
from utils import input_output as io


DATASET_DIR = "./data/input/dataset-sample.csv"
SAVE_PATH = "./data/output/joined-words.json"


def main():
    csv_data_list = io.read_csv(DATASET_DIR)
    total_words_dict = {}

    for i in range(len(csv_data_list)):
        row = csv_data_list[i]

        journal_title, article_title, article_abstract = itemgetter(
            'JOURNAL_TITLE', 'ARTICLE_TITLE', 'ARTICLE_ABSTRACT')(row)

        if article_abstract[-1] != '.':
            article_abstract += '.'

        article_abstract_words = article_abstract.split()

        for j in range(len(article_abstract_words)):
            word = article_abstract_words[j]
        
            if len(word) >= 12 and word not in total_words_dict:
                total_words_dict[word] = word

    with open(SAVE_PATH, 'w') as fout:
        json.dump(total_words_dict , fout, indent=4)


if __name__ == '__main__':
    main()
