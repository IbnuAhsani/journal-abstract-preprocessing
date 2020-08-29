import math


def calculate_tf(word_dict, token_list):
    tf_dict = {}
    token_list_length = len(token_list)

    for word, value in word_dict.items():
        word_count = token_list.count(word)
        tf = word_count / token_list_length
        tf_dict[word] = tf 
    
    return tf_dict


def calculate_tf_idf(tfs, idf):
    tf_idf_dict = {}

    for word, tf in tfs.items():
        if tf == 0:
            tf_idf = tf
        else:
            tf_idf = tf * idf 

        tf_idf_dict[word] = tf_idf
            
    return tf_idf_dict