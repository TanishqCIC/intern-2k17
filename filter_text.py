filename = 'galvin_sections/3.1.txt'
	#Just an array to fetch each word of .txt file as an element to this array
	text = []

	with open(filename,'r') as f:
	    for line in f:
	        for word in line.split():
				text.append(word)
