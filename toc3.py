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
			 cnt += 1
		 else:
			break
	  return int_freq.most_common(cnt)



#print "\n\n********************WELCOME*********************"
#print "\nTOPIC : CONTEXT INFERENCE"
#print "\n"
#print "INPUT SET : User's search history from \" history.txt \"\n"
#print "PLEASE ENTER FOLLOWING DETAILS TO PROCESS YOUR REQUEST\n"



# Ask the user to enter string to search
#search_path = raw_input("Enter directory path to search :\n ")

#file_type = raw_input("File Type : ")
#file_type = ".txt"

#search_str1 = raw_input("Enter the context string :\n ")
#search_str = search_str1.split()
#print search_str
#mylist=[]

# Append a directory separator if not already present
#if not (search_path.endswith("/") or search_path.endswith("\\") ): 
#    search_path = search_path + "/"

# If path does not exist, set search path to current directory
#if not os.path.exists(search_path):

	  def context_inference(search_str):
		  search_path ="."
		  flie_type = ".txt"

# Repeat for each file in the directory  
		  for fname in os.listdir(search_path):

# Apply file type filter   
			  if fname.endswith(file_type):

# Open file for reading
				  fo = open(search_path + fname)

# Read the first line from the file
line = fo.readline()

# Initialize counter for line number
	line_no = 1

# Loop until EOF
	while line != '' :
# Search for string in line
#-----index = line.find(search_str)
#-----if ( index != -1) :
	if any(word in line for word in search_str):
#   print(fname, "[", line_no, ",", index, "] ", line)

		mylist.append(fname.replace(".txt",""))
#-----print mylist


#print fname.replace(".txt","")
#print "---------------------"

#print most_common(mylist)
#most_frequent = integer_frequency(mylist)
#print(most_frequent)




# Read next line
line = fo.readline()  

# Increment line counter
	line_no += 1
#print most_common(mylist)

# most_frequent = integer_frequency(mylist)
#print(most_frequent)


# Close the files
fo.close()


	print "\nMAIN CONTEXT REFERRED HERE IS :\n "
	most_frequent = integer_frequency(mylist)
	print(most_frequent)

	#f = open("history.txt", "a")
	#f.write(search_str1)
	#f.close()
