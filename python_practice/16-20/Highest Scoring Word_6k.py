# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.


def high(x):
    best_word = ""
    max_score = 0

    for word in x.split():
        current_score = 0

        for letter in word:
            score = ord(letter) - 96
            current_score += score

        if current_score > max_score:
            max_score = current_score
            best_word = word

    return best_word


def  high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))




def high(x):
    words = x.split(' ')
    list_scores = []
    for i in words:
        scores = sum([ord(char) - 96 for char in i])
        list_scores.append(scores)
    return words[list_scores.index(max(list_scores))]





example = "hello python im here"
print(high(example))

                