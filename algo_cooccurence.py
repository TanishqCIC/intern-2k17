"""Author -> tanishqcic
   Cluster Innovation Centre, University of Delhi
"""

concepts = []
concepts.append("process management in thread")
concepts.append("management")

#threshold is often defined as e in the paper
threshold = 2



for alpha_index in concepts[:-1]:
	leng_c1 = len(alpha_index)
	leng_c2 = len(alpha_index+1)
	flag_c1 = 0
	flag_c2 = 0
	for beta_index in alpha_index:
		if beta_index == " ":
			flag_c1 = flag_c1+1
	for gamma_index in alpha_index:
		if beta_index == " ":
			flag_c2 = flag_c2+1
	#call function
	"""
	match(flag)

	"""
	print(flag_c1)
	print(flag_c2)
	
"""
#Enter the name of the .txt file  down here
filename = 'galvin_sections/3.1.1.txt'
#Just an array to fetch each word of .txt file as an element to this array
text = []

with open(filename,'r') as f:
    for line in f:
        for word in line.split():
			text.append(word)

#Printing entire .txt file			
print(text)
"""
"""
#introducing the array of concepts here
concepts = []
concepts[0] = 
concepts[1] =

for word in text:
	if word == concepts[0]
"""
