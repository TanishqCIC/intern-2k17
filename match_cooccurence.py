
#flag_alpha over here is flag_alpha+1 in algo_cooccurence.py
#same follows for flag_beta

def match(c1, c2, flag_alpha, flag_beta):

	#Enter the name of the .txt file  down here
	filename = 'galvin_sections/3.1.txt'
	#Just an array to fetch each word of .txt file as an element to this array
	text = []

	with open(filename,'r') as f:
	    for line in f:
	        for word in line.split():
				text.append(word)

	#Printing entire .txt file			
	#print(text)

	count_c1 = 0
	count_c2 = 0
