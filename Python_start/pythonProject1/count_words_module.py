def count_words(text):
    words = text.lower().split()
    count_words_dict = {}
    for el in words:
        count_words_dict[el] = count_words_dict.get(el, 0) + 1
    return count_words_dict


