import filter_text as ft
#flag_alpha over here is flag_alpha+1 in algo_cooccurence.py
#same follows for flag_beta

def match(c1, c2, flag_alpha, flag_beta):

	filename = 'galvin_sections/3.1.txt'
	text = ft.text(filename)

	count_c1 = 0
	count_c2 = 0

	if flag_alpha != 1:
		print('alpha not onegram')
		con_c1 = []
		initial_flag = 0
		for space_alpha in range(0, len(c1)):

			if c1[space_alpha] == " ":
				con_c1.append(c1[initial_flag:space_alpha])
				initial_flag = space_alpha+1
			if space_alpha == len(c1)-1:
				con_c1.append(c1[initial_flag:space_alpha+1])
		print(con_c1)
	else:
		print('alpha is onegram')
		con_c1 = []
		con_c1.append(c1)
		print(con_c1)

	
	if flag_beta != 1:
		print('beta not onegram')
		con_c2 = []
		initial_flag = 0
		for space_beta in range(0, len(c2)):

			if c2[space_beta] == " ":
				con_c2.append(c2[initial_flag:space_beta])
				initial_flag = space_beta+1
			if space_beta == len(c2)-1:
				con_c2.append(c2[initial_flag:space_beta+1])
		print(con_c2)
	else:
		print('beta is onegram')
		con_c2 = []
		con_c2.append(c2)
		print(con_c2)
	
	
	alpha_count = 0
	for cursor_text in range(0, len(text)):
		flag_match = 0
		for cursor_alpha in range(0, len(con_c1)):
			#print('index_text', cursor_text+cursor_alpha, 'ind_alpha', cursor_alpha)
			if cursor_alpha+cursor_text<len(text):
				if text[cursor_text+cursor_alpha] == con_c1[cursor_alpha]:
					if flag_match != 2:
						flag_match = 1
				else:
					flag_match = 2
		if flag_match == 1:
			alpha_count = alpha_count+1
	print('alpha', alpha_count)
	
	beta_count = 0
	for cursor_text in range(0, len(text)):
		flag_match = 0
		for cursor_beta in range(0, len(con_c2)):
			#print('index_text', cursor_text+cursor_alpha, 'ind_alpha', cursor_alpha)
			if cursor_beta+cursor_text<len(text):
				if text[cursor_text+cursor_beta] == con_c2[cursor_beta]:
					if flag_match != 2:
						flag_match = 1
				else:
					flag_match = 2
		if flag_match == 1:
			beta_count = beta_count+1
	print('beta', beta_count)



	"""
	#finding c1 in text
	c1_count = 0
	break_flag = 0
	for cursor_alpha in range(0, len(text)):
		print('break', break_flag)
		for index_alpha in range(0, len(con_c1)):
			if text[cursor_alpha+index_alpha] == con_c1[index_alpha]:
				flag_match = 1
			else:
				flag_match = 0
				break_flag = 1
				break

		if flag_match == 1:
			c1_count = c1_count + 1
	if c1_count != 0:
		print('c1 found', c1_count)
		c1_count=0

	#finding c2 in text
	break_flag = 0
	c2_count = 0
	for cursor_beta in range(0, len(text)):
		for index_beta in range(0, len(con_c2)):
			if text[cursor_beta+index_beta] == con_c1[index_beta]:
				print('text', text[cursor_beta+index_beta], 'concept', con_c1[index_beta])
				flag_match = 1
			else:
				flag_match = 0
				print('flag down')
				break

		if flag_match == 1:
			c2_count = c2_count + 1
	if c2_count != 0:
		print('c2 found', c2_count)
		c2_count = 0
"""
