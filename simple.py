#!/usr/bin/env python2
#coding=utf-8
\
from os import path
import sys
import wordcloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'constitution.txt')).read()
# Separate into a list of (word, frequency).
words = wordcloud.process_text(text)
#words = [(u"你好", 3), ('很好'.decode('utf-8'), 2), ('非常好', 1)]#0.5 0.333 0.16
# Compute the position of the words.
width = 960
height = 600
scale = 1
for i in [0.5, 1,2,3,4,5, 10, 15, 20, 25, 30]:
    print('scale:', i )
    elements = wordcloud.fit_words2(words, width = width / scale, height = height / scale, margin = 2, scale=i)
# Draw the positioned words to a PNG file.
#elements = [(('Bills', 0.015706806282722512), 105, (100.0, 100.0), None)]
#elements = [(('Bills', 0.015706806282722512, 0.0019342359767891767), 100, (0, 0), None)]
#elements = [(('shall', 1.0), 180, (13, 2), None), (('States', 0.418848167539267), 64, (2, 123), None), (('United', 0.28272251308900526), 38, (158, 76), None)]
#print(elements, len(elements))
    wordcloud.draw2(elements, path.join(d, 'constitution.png'), width = width / scale, height = height / scale, scale = scale)
    a = raw_input('press any key')
