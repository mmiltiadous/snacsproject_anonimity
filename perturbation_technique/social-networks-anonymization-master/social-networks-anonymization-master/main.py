# import networkx as nx
# import pandas as pd

# import anonymity
# import graph
# import queries

# from sys import stderr
# from datetime import datetime

#     #    graph.create_ex_graph(),

#     #    graph.create_random_graph(100, 0.05),
#     #    graph.create_random_graph(500, 0.01),
#     #    graph.create_random_graph(1000, 0.005),

#     #    graph.create_scale_free_graph(100),
#     #    graph.create_scale_free_graph(500),
#     #    graph.create_scale_free_graph(1000),

#     #    graph.read_graph('data/enron.txt', 'enron-5'),
#     #    graph.read_graph('data/hepth.txt.gz', 'hepth'),
#     # graph.read_graph('data/emailEu.txt.gz', 'emailEu'),

#     # graph.read_graph('data/RO_edges.csv', 'RO_edges'),

# def main():
#     graphs = [

#     graph.read_graph('data/facebook_combined.txt.gz', 'facebook_combined'),
    
#     ]

#     with open('out2/times.csv', 'a') as f:
#         for g in graphs:
#             compute_graph(g, f)


# def compute_graph(g, f_times=None, draw=False):
#     t1 = datetime.now()

#     print(g.name, file=stderr)

#     if draw:
#         layout = nx.spring_layout(g)

#     measures = {}
#     for pert in [0, .05, .1, .2, .5, 1]:
#         print('  perturbation ({:.0%} of edges)...'.format(pert), file=stderr)

#         pert_graph = anonymity.perturbation(g, pert)
#         if draw:
#             graph.draw_graph(pert_graph, pert, layout)

#         print('    measurements...', file=stderr)
#         measurements = graph.get_measurements(pert_graph)

#         print('    h...', file=stderr)
#         h = [anonymity.deanonymize_h(pert_graph, i) for i in range(0, 5)]

#         print('    edge facts...', file=stderr)
#         ef = [] #[anonymity.deanonymize_edgefacts(g, pert_graph, n) for n in range(0, 51, 10)]

#         measures[pert] = pd.concat([measurements, *h, *ef])

#     t2 = datetime.now()
#     t = t2 - t1

#     print('  execution time: {}'.format(t), file=stderr)

#     if f_times is not None:
#         print('{},{}'.format(g.name, t.total_seconds()), file=f_times)

#     df = pd.DataFrame(measures)
#     # print(df.to_string(), file=stderr)

#     df.to_csv('out/{}.csv'.format(g.name))


# if __name__ == '__main__':
#     main()

import networkx as nx
import pandas as pd
from datetime import datetime

import anonymity
import graph

def read_amazon_graph(file_path):
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                source, target = map(int, line.strip().split())
                G.add_edge(source, target)
    return G

def main():
    file_path = 'Amazon0302.txt'
    amazon_graph = read_amazon_graph(file_path)

    with open('out/amazon.csv', 'a') as f:
        compute_graph(amazon_graph, f)

def compute_graph(g, f_times=None, draw=False):
    t1 = datetime.now()
    print(g.name)

    if draw:
        layout = nx.spring_layout(g)

    measures = {}
    for pert in [0, .05, .1, .2, .5, 1]:
        print('  perturbation ({:.0%} of edges)...'.format(pert))

        pert_graph = anonymity.perturbation(g, pert)
        if draw:
            graph.draw_graph(pert_graph, pert, layout)

        print('    measurements...')
        measurements = graph.get_measurements(pert_graph)

        print('    h...')
        h = [anonymity.deanonymize_h(pert_graph, i) for i in range(0, 5)]

        print('    edge facts...')
        ef = []  # [anonymity.deanonymize_edgefacts(g, pert_graph, n) for n in range(0, 51, 10)]

        measures[pert] = pd.concat([measurements, *h, *ef])

    t2 = datetime.now()
    t = t2 - t1
    print('  execution time: {}'.format(t))

    if f_times is not None:
        print('{},{}'.format(g.name, t.total_seconds()), file=f_times)

    df = pd.DataFrame(measures)
    df.to_csv('out/{}.csv'.format(g.name))

if __name__ == '__main__':
    main()

