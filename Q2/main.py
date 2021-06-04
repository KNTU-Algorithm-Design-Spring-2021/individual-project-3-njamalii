from typing import Union, Dict, Set, List

from graph_draw import create_graph


class node:
    neighbors: Set['node']
    all_nodes: Dict[int, 'node'] = {}

    def __new__(cls, v):
        if v not in cls.all_nodes:
            new_instance = super().__new__(cls)
            new_instance.v = v
            new_instance.neighbors = set()
            cls.all_nodes[v] = new_instance
        else:
            new_instance = cls.all_nodes[v]
        return new_instance

    def is_connected(self, other):
        if not isinstance(other, node):
            other = node(other)
        return other in self.neighbors

    def connect(self, other: Union['node', int]):
        if not isinstance(other, node):
            other = node(other)
        if other in self.neighbors:
            return
        self.neighbors.add(other)
        other.neighbors.add(self)

    def __hash__(self):
        return hash(self.v)

    def __repr__(self):
        return f"||{self.v}-->{','.join(str(i.v) for i in self.neighbors)}"

    def __eq__(self, other):
        if not isinstance(other, node):
            other = node(other)
        return self.v == other.v

    @classmethod
    def clear(cls):
        cls.all_nodes.clear()


def find_route(source: node, dest: node, route: List[node] = None, visited_nodes: Set[node] = None):
    if route is None:
        route = [source]
        visited_nodes = set()
        visited_nodes.add(source)
    if source == dest:
        return [route]
    all_routes = []
    for i in source.neighbors:
        if i not in visited_nodes:
            visited_nodes_ = visited_nodes.copy()
            visited_nodes_.add(i)
            all_routes += find_route(source=i, dest=dest, route=route + [i], visited_nodes=visited_nodes_)
    return all_routes


if __name__ == '__main__':
    case_num = 0
    while 1:
        case_num += 1
        try:
            dest = int(input())
        except EOFError:
            break
        while 1:
            a, b = [int(i) for i in input().split()]
            if a == b == 0:
                break
            node(a).connect(b)
        create_graph(node, case_num=case_num)

        # we created graph, lets search for the proper route
        routes = find_route(node(1), node(dest))
        print(f"case {case_num}")
        for i in routes:
            print(" ".join(str(j.v) for j in i))
            create_graph(node, case_num=case_num, route=i)
        print(f"There are {len(routes)} routes from the firestation to streetcorner {dest}.")
        node.clear()
