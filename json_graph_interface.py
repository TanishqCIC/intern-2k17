print("initializing imports")

import graph_gen as gg
import json
from pprint import pprint

with open('arr_nodes.json') as data_file:    
    data = json.load(data_file)

keys = len(data)

with open('arr_links.json') as data_file:    
    data_links = json.load(data_file)

print(keys)
print(data_links)
arr_nodes = {}

links = []
nodes = []
arr_link = []
all_links = []
key_index = []
for key in data_links:
	list_link = []
	for node in data_links[key]:
		for alpha_index in data_links[key][node]:
			list_link.append(alpha_index)
			all_links.append(alpha_index)
	arr_link.append(list_link)
	key_index.append(key)

print(arr_link)
print(len(arr_link))
for key in data:
	for node in data[key]:
		nodes.append(node)
	arr_nodes['%s' % key] = data[key]
	index = "intrasection_graph"+key
	for beta in range(0, len(key_index)):
		if key_index[beta] == key:
			flag = beta;

	gg.graph(data[key], data_links[key][key], index, flag)
	pprint('done with graph ' + key)
