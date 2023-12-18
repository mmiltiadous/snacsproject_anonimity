import networkx as nx
import pandas as pd

import anonymity
import graph
import queries

from sys import stderr
from datetime import datetime
import pandas as pd


def main():
    graphs = [
    #graph.create_ex_graph(),

    #    graph.create_random_graph(100, 0.05),
    #    graph.create_random_graph(500, 0.01),
    #    graph.create_random_graph(1000, 0.005),

    #    graph.create_scale_free_graph(100),
    #    graph.create_scale_free_graph(500),
    #    graph.create_scale_free_graph(1000),

    #    graph.read_graph('data/enron.txt', 'enron-5'),
    #    graph.read_graph('data/hepth.txt.gz', 'hepth'),
    # graph.read_graph('data/emailEu.txt.gz', 'emailEu'),

    # graph.read_graph('data/RO_edges.csv', 'RO_edges'),

    # graph.read_graph('data/facebook_combined.txt.gz', 'facebook_combined'),
    # read_graph_from_edgelist('data/amazon0302.txt', 'Amazon0302'),
    # read_graph_from_edgelist0('data/fb0.edges', 'fb0'),
    #read_graph_from_edgelist('data/soc-Epinions1.txt', 'soc-Epinions1'),
    read_graph_from_csv('data/musae_git_edges.csv', 'git'),
    ]

    with open('out/times.csv', 'a') as f:
        for g in graphs:
            # Extract a subgraph with 2000 nodes
            subgraph = get_subgraph(g, 5000)
            #undirected_subgraph = g.to_undirected()
            compute_graph(subgraph, f)


def read_graph_from_edgelist0(file_path, name):
    # Read the graph from the edge list text file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    edges = [tuple(map(int, line.strip().split())) for line in lines]

    # Create a directed graph using networkx
    g = nx.DiGraph()
    g.add_edges_from(edges)

    g.name = name
    return g

def read_graph_from_csv(file_path, name):
    # Read the graph from the CSV file
    df = pd.read_csv(file_path, delimiter='\t')

    # Split the 'id_1,id_2' column into two separate columns
    df[['id_1', 'id_2']] = df['id_1,id_2'].str.split(',', expand=True)

    # Convert the columns to integers
    df['id_1'] = df['id_1'].astype(int)
    df['id_2'] = df['id_2'].astype(int)

    # Create a directed graph using networkx
    g = nx.from_pandas_edgelist(df, 'id_1', 'id_2', create_using=nx.DiGraph())

    g.name = name
    return g


def read_graph_from_edgelist(file_path, name):
    # Read the graph from the edge list text file
    g = nx.read_edgelist(file_path, create_using=nx.DiGraph(), nodetype=int, data=(('weight', int),))
    g.name = name
    return g

def get_subgraph(graph, num_nodes):
    # Extract a subgraph with a specified number of nodes
    subgraph_nodes = list(graph.nodes())[:num_nodes]
    subgraph = graph.subgraph(subgraph_nodes)
    
    # Convert the subgraph to an undirected graph
    undirected_subgraph = subgraph.to_undirected()
    
    return undirected_subgraph


def compute_graph(g, f_times=None, draw=False):
    t1 = datetime.now()

    print(g.name, file=stderr)

    if draw:
        layout = nx.spring_layout(g)

    measures = {}
    for pert in [0, .05, .1, .2, .5, 1]:
        print('  perturbation ({:.0%} of edges)...'.format(pert), file=stderr)

        pert_graph = anonymity.perturbation(g, pert)
        if draw:
            graph.draw_graph(pert_graph, pert, layout)

        print('    measurements...', file=stderr)
        measurements = graph.get_measurements(pert_graph)

        print('    h...', file=stderr)
        h = [anonymity.deanonymize_h(pert_graph, i) for i in range(0, 5)]

        # print('    edge facts...', file=stderr)
        # ef = [] #[anonymity.deanonymize_edgefacts(g, pert_graph, n) for n in range(0, 51, 10)]

        measures[pert] = pd.concat([measurements, *h])

    t2 = datetime.now()
    t = t2 - t1

    print('  execution time: {}'.format(t), file=stderr)

    if f_times is not None:
        print('{},{}'.format(g.name, t.total_seconds()), file=f_times)

    df = pd.DataFrame(measures)
    # print(df.to_string(), file=stderr)

    df.to_csv('out/{}.csv'.format(g.name))


if __name__ == '__main__':
    main()


