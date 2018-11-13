import pre
import key
import context
import re
import csv
user = []
with open('input.csv',) as csvfile:
	csvreader = csv.DictReader(csvfile,delimiter='#')
	for row in csvreader:
		#print(row)
		word = row['Input']#"iend didn't reply to my message in whatsapp."
		word = re.sub('[.,!"]','',word)	
		#print (word)
		k = pre.pre_processing(word)
		#print(k)
		l =  (key.keyword_extraction(k))
		inp = []
		print(l)
		for i in l:
			inp.append(i[0])
#print(inp)
		con = context.context_inference(inp)
		print(row['Input'] ,"CONTEXT REFFERED:")
		print(con)
		print("\n")
		temp = []
		for i in con:
			temp.append(i[0])
		user.append(list(temp))
#print (user)
mylist=["sports","education","cultural_festivals","food","family","computer_science","social_media","hospital_and_medicines"]
'''group = []
for i in user:
	temp = []
	for j in i:
		if j in mylist:
			ind = mylist.index(j)
			temp.append(ind)
	group.append(list(temp))
#print(group)'''
for i in mylist:
	k = 1
	print(i,":")
	for x in user:
		if i in x:
			print(k)
		k = k + 1
	#print("\n")
