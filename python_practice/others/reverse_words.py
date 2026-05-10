def reverse_words(text : str):
    new_text = []
    word_list = text.split(" ")
    for word in word_list:
        new_text.append(word[::-1])
    return " ".join(new_text)


def reverse_words(text : str):

    return " ".join([word[::-1] for word in text.split(" ")])

