#!/usr/bin/env python2
#coding=utf-8
from os import path
import wordcloud
from wordcloud import layout_cloud

d = path.dirname(__file__)

width = 800
height = 400
best_elements = None
best_score = 0


#test case 1

text = open(path.join(d, 'constitution.txt')).read()
# Separate into a list of (word, frequency).
words = wordcloud.process_text(text)
#$words = [(u'你好', 3), (u'非常好', 2), (u'大家好', 1)]#0.5 0.333 0.16
# Compute the position of the words.
a = ''
while a != 'e':
    layout_cloud.draw_word_cloud(words, width, height, path.join(d, 'constitution.png'), None)
    a = raw_input('press any key')