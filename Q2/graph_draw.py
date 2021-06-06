import networkx as nx
from matplotlib import pyplot as plt

# ROUTE_EDGE_COLOR = '#f00'
# REGULAR_EDGE_COLOR = '#fff'
ROUTE_EDGE_COLOR = 'r'
REGULAR_EDGE_COLOR = 'b'


def create_graph(node_class, case_num=None, route=None):
    if route is not None:
        route = set(zip(route, route[1:]))
    else:
        route = []
    graph = nx.Graph()
    for node_num, node_instance in node_class.all_nodes.items():
        for connected_node in node_instance.neighbors:
            graph.add_edge(node_instance.v, connected_node.v)
    if case_num is not None:
        colors = [ROUTE_EDGE_COLOR if (u, v) in route or (v, u) in route else REGULAR_EDGE_COLOR for u, v in
                  graph.edges()]
        draw_graph(graph, f"main graph #case{case_num}", colors=colors)
    return graph


def draw_graph(graph, title, colors):
    pos = nx.circular_layout(graph)

    nx.draw(graph, pos,
            edge_color=colors,
            with_labels=True,
            node_color='lightgreen')
    plt.title(title)
    plt.show()
