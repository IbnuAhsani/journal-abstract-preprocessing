import json
from utils import input_output, text_preprocessing


DATASET_DIR = './data/input/dataset-sample.csv'
SAVE_DIR = './data/preprocessed-dataset-sample.json'


def main():

    csv_data = input_output.read_csv(DATASET_DIR)
    total_process_count = len(csv_data) 
    current_process_count = 1
    preprocessed_data = []

    print("total data count: ", total_process_count)

    for row in csv_data:
        JOURNAL_ID, JOURNAL_TITLE, ARTICLE_ID, ARTICLE_TITLE, ARTICLE_ABSTRACT  = row.values()

        if current_process_count % 50 == 0:
            print("processing data num: ", current_process_count)

        tokens = text_preprocessing.generate_tokens(ARTICLE_ABSTRACT)
        tokens_seen = set()
        tokens_duplicate_removed = []

        for item in tokens:
            if item not in tokens_seen:
                tokens_seen.add(item)
                tokens_duplicate_removed.append(item)

        temp_dict = {
            "JOURNAL_ID": int(JOURNAL_ID),
            "JOURNAL_TITLE": JOURNAL_TITLE,
            "ARTICLE_ID": int(ARTICLE_ID),
            "ARTICLE_TITLE": ARTICLE_TITLE,
            "ARTICLE_ABSTRACT": ARTICLE_ABSTRACT,
            "TOKENS": tokens,
            "TOKENS_DUPLICATE_REMOVED": tokens_duplicate_removed
        } 

        preprocessed_data.append(temp_dict)
        current_process_count += 1
    
    with open(SAVE_DIR, 'w') as fout:
        json.dump(preprocessed_data , fout, indent=4)


if __name__ == '__main__':
    main()