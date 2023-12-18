# external python modules
import networkx
import random
import pandas as pd
import io
from statistics import median
import numpy as np

# internal python modules
import generalized_graph
import partitioner

group_size = 10
tmp_dir = "/tmp/"
random.seed(2024)

def get_subgraph(graph, num_nodes):
    # Extract a subgraph with a specified number of nodes
    subgraph_nodes = list(graph.nodes())[:num_nodes]
    subgraph = graph.subgraph(subgraph_nodes)
    
    # Convert the subgraph to an undirected graph
    undirected_subgraph = subgraph.to_undirected()
    
    return undirected_subgraph



### INPUT GRAPH 


#### Facebook ####

# with open('Datasets/facebook/0.edges.edges', 'r') as file:
#     data = file.read()
# print(data)

# data = data.decode('utf-8')

# # convert into a NetworkX graph
# fb_graph = networkx.Graph()

# # add edges to the graph
# for i, line in enumerate(io.StringIO(data)):
#     node1, node2 = map(int, line.split())
#     fb_graph.add_edge(node1, node2)

# input_graph = fb_graph
# file_name = 'out/fb.txt'


# #### DBLP ####

# with open('Datasets/dblp/com-dblp.ungraph.txt', 'r') as file:
#     data = file.read()
# data = data[115:] 
# print(data)

# data = data.decode('utf-8')

# # convert into a NetworkX graph
# dblp_graph = networkx.Graph()

# # add edges to the graph
# for i, line in enumerate(io.StringIO(data)):
#     node1, node2 = map(int, line.split())
#     dblp_graph.add_edge(node1, node2)

# dblp_subgraph = get_subgraph(dblp_graph, num_nodes = 3000)

# input_graph = dblp_subgraph
# file_name = 'out/dblp.txt'



#### GitHub ####

df = pd.read_csv("Datasets/github/musae_git_edges.csv")
print(df)
github_graph = networkx.from_pandas_edgelist(df, source='id_1', target='id_2')
github_subgraph = get_subgraph(github_graph, num_nodes = 5000)

input_graph = github_subgraph
file_name = 'out/github_5000_2.txt'



# #### Amazon ####

# with open('Datasets/amazon/amazon0302.txt', 'r') as file:
#     data = file.read()  
# data = data[190:]  
# print(data)

# data = data.decode('utf-8')

# # convert into a NetworkX graph
# amazon_graph = networkx.Graph()

# # add edges to the graph
# for i, line in enumerate(io.StringIO(data)):
#     node1, node2 = map(int, line.split())
#     amazon_graph.add_edge(node1, node2)

# amazon_subgraph = get_subgraph(amazon_graph, num_nodes = 3000)

# input_graph = amazon_subgraph
# file_name = 'out/amazon_3000.txt'



# ###### Epinions ######

# with open('Datasets/epinions/soc-Epinions1.txt', 'r') as file:
#     data = file.read()  
# data = data[168:]  
# print(data)

# data = data.decode('utf-8')

# # convert into a NetworkX graph
# epinions_graph = networkx.Graph()

# # add edges to the graph
# for i, line in enumerate(io.StringIO(data)):
#     node1, node2 = map(int, line.split())
#     epinions_graph.add_edge(node1, node2)

# epinions_subgraph = get_subgraph(epinions_graph, num_nodes = 2000)

# input_graph = epinions_subgraph
# file_name = 'out/epinions.txt'






# RUN PARTITIONING ALGORITHM
# partitioner.debug = True # turn on debugging
# partitioner.debug_sampling = True
my_partitioner = partitioner.MinNumWorldsPartitioner(g=input_graph, k=group_size, working_dir=tmp_dir, max_steps=5000)
p = my_partitioner.partition()

print "Printing the node partition"
grp_cnt = 1
for grp in p:
	print "Group #%d, Members:" % grp_cnt,
	print p.get_members(grp)
	grp_cnt += 1


out = open(file_name, "w")
out.close()

# SAMPLE SIMPLE GRAPH FROM GENERALIZED GRAPH
gen_graph = generalized_graph.GeneralizedGraph(input_graph, p, alg="Hay et al. 2008", k=group_size)
print "Created generalized graph"

sampled_graph = gen_graph.sample_graph()
print "Sampled a simple graph from generalized graph"

## Nodes & Edges
print "Input graph has %d nodes and %d edges" % (input_graph.number_of_nodes(), input_graph.number_of_edges())
print "Sampled graph has %d nodes and %d edges" % (sampled_graph.number_of_nodes(), sampled_graph.number_of_edges())
out = open(file_name, "a")
out.write("Input graph has %d nodes and %d edges" % (input_graph.number_of_nodes(), input_graph.number_of_edges()) + "\n" + "Sampled graph has %d nodes and %d edges" % (sampled_graph.number_of_nodes(), sampled_graph.number_of_edges())  + "\n")
out.close()

## Average Clustering Coefficient
orig_clustering = networkx.average_clustering(input_graph)
clustering = networkx.average_clustering(sampled_graph)
print "Input graph had clustering coefficient of %0.2g\nSampled graph has clustering of %0.2g" % (orig_clustering, clustering)	
out = open(file_name, "a")
out.write("Input graph had clustering coefficient of %0.2g\nSampled graph has clustering of %0.2g" % (orig_clustering, clustering)  + "\n")
out.close()

## Number of Connected Components
orig_cc = networkx.number_connected_components(input_graph)
cc = networkx.number_connected_components(sampled_graph)
print "Input graph had number of connected components of %0.2g\nSampled graph has number of connected components of %0.2g" % (orig_cc, cc)
out = open(file_name, "a")
out.write("Input graph had number of connected components of %0.2g\nSampled graph has number of connected components of %0.2g" % (orig_cc, cc)  + "\n")
out.close()


## Degree Centrality
orig_dcentr = median(networkx.degree_centrality(input_graph).values())
dcentr = median(networkx.degree_centrality(sampled_graph).values())
print "Input graph had Degree Centrality of %0.2g\nSampled graph has Degree Centrality of %0.2g" % (orig_dcentr, dcentr)
out = open(file_name, "a")
out.write("Input graph had Degree Centrality of %0.2g\nSampled graph has Degree Centrality of %0.2g" % (orig_dcentr, dcentr)  + "\n")
out.close()

## Average Degree
orig_avdegree = np.mean(list(dict(input_graph.degree()).values()))
avdegree = np.mean(list(dict(sampled_graph.degree()).values()))
print "Input graph had Average Degree of %0.2g\nSampled graph has Average Degree of %0.2g" % (orig_avdegree, avdegree)
out = open(file_name, "a")
out.write("Input graph had Average Degree of %0.2g\nSampled graph has Average Degree of %0.2g" % (orig_avdegree, avdegree)  + "\n")
out.close()

## Transitivity
orig_trans = networkx.transitivity(input_graph)
trans = networkx.transitivity(sampled_graph)
print "Input graph had Transitivity of %0.2g\nSampled graph has Transitivity of %0.2g" % (orig_trans, trans)
out = open(file_name, "a")
out.write("Input graph had Transitivity of %0.2g\nSampled graph has Transitivity of %0.2g" % (orig_trans, trans)  + "\n")
out.close()


