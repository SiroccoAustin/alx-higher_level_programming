#!/usr/bin/python3

"""Declare text indention function"""

def text_indentation(text):
    """Separates sentences in a given piece of text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    sentences = []
    start = 0
    text_len = len(text)

    while start < text_len:
        while start < text_len and text[start] == ' ':
            start += 1

        end = start
        while end < text_len and text[end] not in ['.', ':', '?']:
            end += 1
        if end < text_len:
            end += 1
        sentence = text[start:end]
        sentences.append(sentence.strip())
        start = end
    for sentence in sentences:
        print(sentence)
