def total_price(items):
    return sum(items)

def sort_strings(s):
    return sorted(s)

def count_words(sentence):
    words=sentence.split()
    word_count ={}
    for word in words:
        word_count[word]= word_count.get(word,0)+1
    return word_count