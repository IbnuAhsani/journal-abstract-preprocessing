import math


def calculate_tf(word_dict, token_list):
    tf_dict = {}
    token_list_length = len(token_list)

    for word, value in word_dict.items():
        word_count = token_list.count(word)
        tf = word_count / token_list_length
        tf_dict[word] = tf 
    
    return tf_dict


def calculate_tf_idf(tf):
    tf_idf_dict = {}

    for word, val in tf.items():
        if val == 0:
            tf_idf = val
        else:
            tf_idf = val * math.log(1/2)

        tf_idf_dict[word] = tf_idf
            
    return tf_idf_dict