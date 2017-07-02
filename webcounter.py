import os
import re
import collections
from collections import Counter

commonwords = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at"]
weirdwords = ["image", "s"]

print("I'd love to help you find the most common words on any website!")
website = input("Please enter website here \n:")

result = os.popen("wget -O test.html {} --no-check-certificate && curl -H 'Accept: text/plain' -T test.html http://localhost:9998/tika".format(website)).read()
rawwords = result

wordList = re.sub("[^\w]", " ", rawwords).split()
lowerwordList = map(str.lower, wordList)
editedWordList = []


exclusions = int(input("how many, up to 20, words would you like to exclude? \n: "))
selectedCommonwords = commonwords[0:(exclusions-1)]
for x in lowerwordList:
    if x not in selectedCommonwords + weirdwords:
        editedWordList.append(x)
howmany = int(input("How many top words would you like? \:"))
print(Counter(editedWordList).most_common(howmany))

wordcount = collections.defaultdict(int)
for word in lowerwordList:
    wordcount[word] += 1

items = wordcount.items()
word_tuples = list(items)

sortedlist = sorted(word_tuples, key=lambda x: x[1], reverse=True)
print(sortedlist[:20])