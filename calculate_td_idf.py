import csv
import json
from collections import OrderedDict
from utils import tf_idf


FV_TOKENS_DIR = 'data/fv-tokens.json'
DATA_JSON_DIR = 'data/data-sample.json'
SAVE_DIR = './data/tf-idf.csv'


def main():

    with open(FV_TOKENS_DIR) as f:
      fv_token_list = json.load(f)
    
    fv_token_dict = OrderedDict({ i : 0 for i in fv_token_list})

    with open(DATA_JSON_DIR) as f:
        datas = json.load(f)

    tf_list = []

    for data in datas:
        article_id = data['ARTICLE_ID']
        journal_id = data['JOURNAL_ID']
        tokens = data['TOKENS']

        if(int(article_id) % 500 == 0):
            print("processing article_id: ", article_id)

        tfs = tf_idf.calculate_tf(fv_token_dict, tokens)
        
        temp_tf_list = []

        for tf in tfs.values():
            temp_tf_list.append(tf) 
        
        temp_tf_list.append(journal_id)
        tf_list.append(temp_tf_list)

    with open(SAVE_DIR, 'w', newline="") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, quotechar='', escapechar='\\')
        wr.writerows(tf_list)


if __name__ == '__main__':
    main()