def char_count(sentence):
    data={}
    for char in set(sentence):
        data[char]=sentence.count(char)
    return data   

def word_count(sentence):
    data={}
    words=sentence.split()
    for word in set(words):
        data[word]=sentence.count(word)
    return data 