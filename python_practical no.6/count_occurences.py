# program to count occurences of all words in a sentence
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
print( word_count("The quick brown for jumps over the lazy dog."))

