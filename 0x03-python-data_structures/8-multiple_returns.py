#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_tuple = ()
    count = 0
    first = sentence[0] if sentence else None
    for word in sentence:
        count = count + 1

    sentence_tuple = (count, first)
    return sentence_tuple
