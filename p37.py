# -*- coding: utf-8 -*-

import pylab
import re
import collections

with open("neko.txt.mecab") as f:
	neko_txt = f.read()

neko_morpheme = []
sent_lst = neko_txt.split("EOS\n")

#surface（表層形）、base（基本形）、pos（品詞）、pos1（品詞細分類1）
for sent in sent_lst: 
	morpheme_lst = sent.split("\n")
	sent_data = []
	for morpheme in morpheme_lst:
		if len(morpheme) < 2:
			continue
		morpheme_data = morpheme.split("\t")[1].split(",")
		base = morpheme_data[6]
		pos = morpheme_data[0]
		pos1 = morpheme_data[1]
		morpheme_dict = {'surface':morpheme.split("\t")[0], 'base':base, 'pos':pos, 'pos1':pos1}
		sent_data.append(morpheme_dict)
	neko_morpheme.append(sent_data)


wc = collections.Counter()
for sent in neko_morpheme:
	for ele in sent:
		wc[ele['surface']] += 1

for k, v in sorted(wc.items(), key=lambda x: x[1], reverse=True)[:10]:
	print k, v
	
x = pylab.arange(-10.0, 10.0, 0.1)

y = pylab.sin(x)

pylab.plot(x, y)

#pylab.show()
