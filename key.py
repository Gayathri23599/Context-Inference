import nltk
def keyword_extraction(inp):
	f = open("punctuation.txt","r")
	fp = f.readline()
	pos = nltk.pos_tag(inp)
	l = []
	ret = []
	#print(pos)
	while fp != '':
		l.append(fp.rstrip())
		fp = f.readline()
	k = 0
	for i in inp:
		s = -1
		temp = []
		ind = inp.index(i)
		if pos[ind][1] == 'NN':
			s = 1
		try:
			j = ret.index(i)
			score = ret[j][1]
		except:
			score = 0
		if i.lower() in l:	
			score += s*0.5
		else:
			score += s*1
		try:
			ret[j][1] = score
		except:
			temp.append(i)
			temp.append(score)
		ret.append(list(temp))
		k = k + 1
	ret = sorted(ret,key=lambda l:l[1], reverse = True)
	print (ret)
	return ret[:3]
