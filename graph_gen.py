#Author -> TanishqCIC

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as ml
from pylab import rcParams
import igraph as ig
import networkx as nx
import seaborn as sb 

print('Cheers! imports done')

def graph(nodes, links, index, flag):
	arr = []
	arr = nodes;
	print(arr);
	rcParams['figure.figsize'] = 5,4
	sb.set_style('whitegrid')

	G = nx.Graph()	
	G.add_nodes_from(arr)
	G.add_edges_from(links)
	string = 'nodes: '+str(len(arr))
	
	string = 'edges: '+str(len(links))
	
	if flag == 1:
		nx.draw(G, node_color='bisque', with_labels=True, node_size=50, font_size=0.4)	
	else:
		nx.draw(G, node_color='bisque', with_labels=True, node_size=300, font_size=2)
	
	plot = index+".png"
	ml.savefig(plot, dpi=2800)
	ml.savefig("plot.pdf")
	ml.clf()

	arr = []
	links = []
	G.clear()
