import csv
import json
from collections import OrderedDict
from utils import tf_idf


STOP_WORD_DIR = './data/input/stop-words.json'
DATA_JSON_DIR = './data/input/data-sample.json'
SAVE_DIR = './data/data-sample-stop-words-removed.json'


def main():

    with open(STOP_WORD_DIR) as f:
      stop_words = json.load(f)

    with open(DATA_JSON_DIR) as f:
        datas = json.load(f)

    processed_data = []

    for data in datas:
        journal_id = data['JOURNAL_ID']
        journal_title = data['JOURNAL_TITLE']
        article_id = data['ARTICLE_ID']
        article_title = data['ARTICLE_TITLE']
        article_abstract = data['ARTICLE_ABSTRACT']
        tokens = data['TOKENS']
        tokens_dpl_removed = data['TOKENS_DUPLICATE_REMOVED']
        
        tokens_sw_removed = [token for token in tokens if token not in stop_words]
        tokens_dpl_removed_sw_removed = [token for token in tokens_dpl_removed if token not in stop_words]

        temp_dict = {
            "JOURNAL_ID": int(journal_id),
            "JOURNAL_TITLE": journal_title,
            "ARTICLE_ID": int(article_id),
            "ARTICLE_TITLE": article_title,
            "ARTICLE_ABSTRACT": article_abstract,
            "TOKENS": tokens_sw_removed,
            "TOKENS_DUPLICATE_REMOVED": tokens_dpl_removed_sw_removed
        } 

        processed_data.append(temp_dict)

    with open(SAVE_DIR, 'w') as fout:
        json.dump(processed_data , fout, indent=4)


if __name__ == '__main__':
    main()