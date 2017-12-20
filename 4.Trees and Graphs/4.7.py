# -*- coding: utf-8 -*-

"""
Question 4.7:
    Build order: You are given a list of projects and a list of dependencies(which is a list of pairs of projects,
                 where the second project is dependent on the first project). All of a project's dependencies must
                 be built before the project is. Find a build order that will allow the projects to be built. If
                 there is no valid build order, return an error.
    EXAMPLE:
        Input:
            projects: a, b, c, d, e, f
            dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
        Output: f, e, a, b, d, c
"""


class Graph:
    def __init__(self):
        self.nodes = []
        self.links = []

    def add_node(self, s):
        self.nodes.append(s)

    def add_link(self, s, t):
        self.links.append([s, t])

    def del_node(self, s):
        for link in self.links:
            if s in link:
                self.links.remove(link)
        if s in self.nodes:
            self.nodes.remove(s)
        else:
            raise Exception('Delete Node Error!')

    def del_link(self, s, t):
        if [s, t] in self.links:
            self.links.remove([s, t])
        elif [t, s] in self.links:
            self.links.remove([t, s])
        else:
            raise Exception('Delete Link Error!')


def get_graph():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')

    g.add_link('a', 'd')
    g.add_link('f', 'b')
    g.add_link('b', 'd')
    g.add_link('f', 'a')
    g.add_link('d', 'c')
    return g


def get_order(graph):
    """
    Take O(n2*m) time and O(n) space
    :param graph: Input Graph
    :return: Output Order
    """
    order = []
    times = len(graph.nodes)
    for _ in range(times):
        for node in graph.nodes:
            flag = True
            for link in graph.links:
                if node == link[1]:
                    flag = False
            if flag:
                if node not in order:
                    order.append(node)
                for link in graph.links:
                    if node == link[0]:
                        graph.del_link(link[0], link[1])
    return order


if __name__ == '__main__':
    print(get_order(get_graph()))
