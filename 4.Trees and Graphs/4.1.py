# -*- coding: utf-8 -*-

"""
Question 4.1:
    Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between
                         two nodes.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.state = 'Unvisited'


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


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


def haveRoute(g, s, t):
    """
    Take O(n + l) time and O(n) space
    :param g: Graph
    :param s: Node s
    :param t: Node t
    :return: Result
    """
    q = Queue()
    q.enqueue(s)
    while not q.isEmpty():
        op = q.dequeue()
        for link in g.links:
            if op == link[0]:
                n = link[1]
                if n == t:
                    return True
                if n.state == 'Unvisited':
                    q.enqueue(n)
            elif op == link[1]:
                n = link[0]
                if n == t:
                    return True
                if n.state == 'Unvisited':
                    q.enqueue(n)
        op.state = 'Visited'
    return False


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    g = Graph()
    g.add_node(a)
    g.add_node(b)
    g.add_node(c)
    g.add_link(a, b)
    g.add_link(a, c)
    print(haveRoute(g, b, d))
