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
		score = -1
		temp = []
		temp.append(i)
		ind = inp.index(i)
		if pos[ind][1] == 'NN':
			score = 1
		if i.lower() in l:	
			#score += score*0.5
			temp.append(score)
		else:
			#score += score
			temp.append(score)
		ret.append(list(temp))
		k++;
	ret = sorted(ret,key=lambda l:l[1], reverse = True)
	print (ret)
	return ret[:3]
