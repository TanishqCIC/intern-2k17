"""Author -> tanishqcic
   Cluster Innovation Centre, University of Delhi
"""

import match_cooccurrence as mc

concepts = []
#concepts from section 3.1
concepts.append("process control block")
concepts.append("task control block")
concepts.append("multithreaded processes")
concepts.append("CPU-scheduling")
concepts.append("Memory-management")
concepts.append("task")
#concepts from 3.3
concepts.append("system call")
concepts.append("process execution")


filenames = []
filenames.append('galvin_sections/3.1.txt')
filenames.append('galvin_sections/3.2.txt')
filenames.append('galvin_sections/3.3.txt')

print('Sections Involved', filenames)
#threshold is often defined as e in the paper
threshold = 0
array = []

for alpha in range(0, len(concepts)):
	for beta in range(alpha+1, len(concepts)):
		flag_alpha = 0
		flag_beta = 0
		c1 = concepts[alpha]
		c2 = concepts[beta]
		for space_alpha in range(0, len(concepts[alpha])):
			if c1[space_alpha] == " ":
				flag_alpha = flag_alpha+1
		for space_beta in range(0, len(concepts[beta])):
			if c2[space_beta] == " ":
				flag_beta = flag_beta+1
		#print('pairs', alpha, beta)
		#print('flags', flag_alpha+1, flag_beta+1)
		#call function
		

		alpha_count, beta_count = mc.match(c1, c2, flag_alpha+1, flag_beta+1, filenames)
		raw = (c1, alpha_count, c2, beta_count)
		array.append(raw)
		#print('-----')
#print(array)
print('-------')
print('total links possible', len(array))

link = []
for elements in array:
	turn = 0
	concept_1 = elements[0]		
	concept_2 = elements[2]
	for flags in range(0, len(elements[1])):
		if elements[1][flags] > 0:
			if elements[3][flags] > 0:
				turn = turn + 1
	#print(turn)
	if turn > threshold:
		link_concepts = (concept_1, concept_2)
		link.append(link_concepts)
print('-------')
print('LINKED CONCEPTS', len(link))
print('-------')
for concepts in link:
	to_print = (concepts[0] + ' & ' + concepts[1])
	print(to_print)
#print(link)
print('-------')
print('www.github.com/TanishqCIC')






















"""
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
	match(flag)

	"""
	#print(flag_c1)
	#print(flag_c2)
	
