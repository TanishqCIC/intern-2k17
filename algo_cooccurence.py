"""Author -> tanishqcic
   Cluster Innovation Centre, University of Delhi
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

#introducing the array of concepts here
concepts = []
concepts[0] = 
concepts[1] =

for word in text:
	if word == concepts[0]
