import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import itertools as it


# function for drawing a non-directional network graph - adapted from NetworkX examples
def draw_graph(graph, node_color, edge_color, title, labels=None, graph_layout='shell',
               node_size=1600, node_alpha=0.4,
               node_text_size=12, edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='serif'):

    # create networkx graph
    G=nx.MultiGraph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    edgewidth=[]
    for (u,v,d) in G.edges(data=True):
        edgewidth.append(5*len(G.get_edge_data(u,v)))

    nodesize = []
    for (u,v,d) in G.edges(data=True):
        nodesize.append(u)
        nodesize.append(v)
        # print nodesize
    bigball = [nodesize.count(v)*750 for v in G]

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=bigball,
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edgewidth,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font, font_weight='bold')

    if labels is None:
        # labels = range(len(graph))
        labels = ''

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
                                 label_pos=edge_text_pos)

    font = {'fontname': 'Helvetica',
            'color': 'k',
            'fontweight': 'bold',
            'fontsize': 18}
    plt.title(title, font)

    # show graph
    plt.axis('off')
    plt.show()


# function for reading in assist log CSV files
def read_assists_csv(filename):
    with open(filename) as myFile:
        # learnt my lesson about using splitlines() instead of readlines()
        dataLines = myFile.read().splitlines()

    data_temp = []
    for z in range(0, len(dataLines)):
        data_temp.append(dataLines[z].split(','))
        print data_temp[z-1]

    tags = []
    for i in range(len(data_temp)):
        temp = []
        for j in range(0, len(data_temp[0])):
            if data_temp[i][j] != '' and data_temp[i][j] != '\r\n':
                temp.append(str(data_temp[i][j]))

        tags.append(temp)

    # prepare assist data in graph format where each connection is one edge,
    # and the players involved are the two nodes...['Node1', 'Node2']
    graph = []
    for i in range(len(tags)):
        temp_tags = list(it.combinations(tags[i], 2))
        for n in temp_tags:
            graph.append(n)

    return graph

# Load in graphs for both teams from all 7 games
graph1 = read_assists_csv("source assist logs/dubsG1asts.csv")
graph2 = read_assists_csv("source assist logs/cavsG1asts.csv")

graph3 = read_assists_csv("source assist logs/dubsG2asts.csv")
graph4 = read_assists_csv("source assist logs/cavsG2asts.csv")

graph5 = read_assists_csv("source assist logs/dubsG3asts.csv")
graph6 = read_assists_csv("source assist logs/cavsG3asts.csv")

graph7 = read_assists_csv("source assist logs/dubsG4asts.csv")
graph8 = read_assists_csv("source assist logs/cavsG4asts.csv")

graph9 = read_assists_csv("source assist logs/dubsG5asts.csv")
graph10 = read_assists_csv("source assist logs/cavsG5asts.csv")

graph11 = read_assists_csv("source assist logs/dubsG6asts.csv")
graph12 = read_assists_csv("source assist logs/cavsG6asts.csv")

graph13 = read_assists_csv("source assist logs/dubsG7asts.csv")
graph14 = read_assists_csv("source assist logs/cavsG7asts.csv")

# show graphs
draw_graph(graph1, '#E2B70B', 'b', "Mapping GSW Assists in Finals G1")
draw_graph(graph2, '#CCCC00', '#830A0A', "Mapping CAVS Assists in Finals G1")

draw_graph(graph3, '#E2B70B', 'b', "Mapping GSW Assists in Finals G2")
draw_graph(graph4, '#CCCC00', '#830A0A', "Mapping CAVS Assists in Finals G2")

draw_graph(graph5, '#E2B70B', 'b', "Mapping GSW Assists in Finals G3")
draw_graph(graph6, '#CCCC00', '#830A0A', "Mapping CAVS Assists in Finals G3")

draw_graph(graph7, '#E2B70B', 'b', "Mapping GSW Assists in Finals G4")
draw_graph(graph8, '#CCCC00', '#830A0A', "Mapping CAVS Assists in Finals G4")

draw_graph(graph9, '#E2B70B', 'b', "Mapping GSW Assists in Finals G5")
draw_graph(graph10, '#CCCC00', '#830A0A', "Mapping CAVS Assists in Finals G5")

draw_graph(graph11, '#E2B70B', 'b', "Mapping GSW Assists in Finals G6")
draw_graph(graph12, '#CCCC00', '#830A0A', "Mapping CAVS Assists in Finals G6")

draw_graph(graph13, '#E2B70B', 'b', "Mapping GSW Assists in Finals G7")
draw_graph(graph14, '#CCCC00', '#830A0A', "Mapping CAVS Assists in Finals G7")
