

import json
import pandas as pd
data = []
tweets = []

for line in open('ambitionFilmESA.json', 'r'):
    a,b = line.split('\ufeff')
    data.append(a)

for x in data:
    l,m = x.split(': "')
    tweets.append(m)

with open("Tweets.txt", "w") as text_file:
    for k in tweets:
        text_file.write(k + '\n')






