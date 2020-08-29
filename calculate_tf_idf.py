import csv
import json
import math
from collections import OrderedDict
from utils import tf_idf


FV_TOKENS_DIR = './data/input/fv-tokens.json'
DATA_JSON_DIR = './data/input/data-sample.json'
TF_IDF_LOG_SAVE_DIR = './data/output/tf-idf-log.json'
TF_IDF_VALUE_SAVE_DIR = './data/output/tf-idf-value.csv'


def main():

    with open(FV_TOKENS_DIR) as f:
      fv_token_list = json.load(f)
    
    fv_token_dict = OrderedDict({ i : 0 for i in fv_token_list})

    with open(DATA_JSON_DIR) as f:
        datas = json.load(f)

    tf_idf_log = []
    tf_idf_list = []
    abstract_num = 1
    counter = 1

    for data in datas:
        article_id = data['ARTICLE_ID']
        journal_id = data['JOURNAL_ID']
        tokens_dupl_removed = data['TOKENS_DUPLICATE_REMOVED']

        if counter % 500 == 0:
            print("processing article num: ", counter)

        idf = math.log10(0.5)
        tfs = tf_idf.calculate_tf(fv_token_dict, tokens_dupl_removed)
        tf_idfs = tf_idf.calculate_tf_idf(tfs, idf)

        for key in tfs.keys():
            tf_val = tfs[key]
            tf_idf_val = tf_idfs[key]

            if tf_val == 0:
                idf_val = 0
            else:
                idf_val = idf
        
            temp_dict = {
                "TOKEN": key,
                "ABSTRACT_NO": abstract_num,
                "TF": tf_val,
                "IDF": idf_val,
                "TF_IDF": tf_idf_val
            }

            tf_idf_log.append(temp_dict)
        
        temp_tf_idf_list = []

        for tfidf in tf_idfs.values():
            temp_tf_idf_list.append(tfidf) 
        
        temp_tf_idf_list.append(journal_id)
        tf_idf_list.append(temp_tf_idf_list)

        abstract_num += 1
        counter += 1

    with open(TF_IDF_LOG_SAVE_DIR, 'w') as fout:
        json.dump(tf_idf_log , fout, indent=4)

    with open(TF_IDF_VALUE_SAVE_DIR, 'w', newline="") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, quotechar='', escapechar='\\')
        wr.writerows(tf_idf_list)


if __name__ == '__main__':
    main()