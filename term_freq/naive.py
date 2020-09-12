# This is a naive approach that uses the built-in Python collections.Counter
#

from collections import Counter

punctuation = ['“','”', '.', ',']
stop_words = ['a', 'an', 'the', 'of', 'it', 'is', '', 'and', 'to']

def term_freq(doc, n = 10, punctuation= [], stop_words = []):
    # Make every word small letters
    doc = doc.lower()

    # Remove punctiation
    for p in punctuation:
        doc = doc.replace(p, "")
    
    # Come back to this for clearer code
    lines = [line.split(' ') for line in doc.split('\n')]
    words =  [word for sentence in lines for word in sentence]

    # Remove stop words
    words = [word for word in words if word not in stop_words]
    
    # Count the words
    return Counter(words).most_common(n)

with open('pride.txt', encoding='utf8') as f:
    doc = f.read()
    term_freqs = term_freq(doc, punctuation = punctuation, stop_words = stop_words)
    for tf in term_freqs:
        print(tf)

