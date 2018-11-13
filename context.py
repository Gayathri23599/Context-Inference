import os
from collections import Counter

def integer_frequency(int_list):
	int_freq = Counter()
	for i in int_list:
		int_freq[i] += 1
		cnt = 0
		values = sorted(int_freq.values())
		values.reverse()
		for x in values:
			if x == values[0]:
				global cnt
				cnt += 1
			else:
				break
	return int_freq.most_common(cnt)

def context_inference(search_str):
	search_path ="./"
	file_type = ".txt"
	mylist = []
	for fname in os.listdir(search_path):
		if fname.endswith(file_type):
			fo = open(search_path + fname,"r")
			line = fo.readline()
			line_no = 1
			while line != '' :
				if any(word in line for word in search_str):
					mylist.append(fname.replace(".txt",""))
				line = fo.readline()
				line_no += 1
			fo.close()
	#print ("\nMAIN CONTEXT REFERRED HERE IS :\n")
	most_frequent = integer_frequency(mylist)
	return most_frequent
