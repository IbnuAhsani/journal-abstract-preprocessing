def calculate_tf(word_dict, token_list):
    tf_dict = {}
    token_list_length = len(token_list)

    for word, value in word_dict.items():
        word_count = token_list.count(word)
        tf = word_count / token_list_length
        tf_dict[word] = tf 
    
    return tf_dict


def calculate_idf(documents):
    num_documents = len(documents)
    idf_dict = dict.fromkeys(documents[0].keys(), 0)

    for document in documents:
        for word, val in document.items():
            if val > 0:
                idf_dict[word] += 1
    
    for word, val in idf_dict.items():
        idf_dict[word] = 1 + math.log(num_documents / float(val + 1))
    
    return idf_dict


def calculate_tf_idf(tf, idf):
    tf_idf = {}

    for word, val in tf.items():
        if val not in idf:
            word_idf = 1
        else:
            word_idf = idf[word]

        tf_idf[word] = val * word_idf
            
    return tf_idf