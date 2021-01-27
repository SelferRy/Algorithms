from heap import Prior_queue

class Graph(object):

    def __init__(self, graph_dict={}):
        self._vertices = graph_dict
        self._edges = None
        self.d = {}
        self.p = {}
        self._weights = None
        # self.edges = self.get_edges

    @property
    def vertices(self):
        return self._vertices

    @property
    def weights(self):
        if self._weights == None:
            self._weights = {f"{v}, {u[0]}": u[1] for v in [*self._vertices] for u in self._vertices[v]}
        return self._weights
        # u = self.vertices[u]
        # for i in []

# ==========================================
    def v(self, vert):
        return self._path_info[vert]

    @property
    def edges(self):
        if self._edges == None: # or [*self.graph_dict] != [v[0] for v in self._edges]:
            self._edges = self.get_edges()
        return self._edges

    def get_edges(self):
        edges = [[v, u[0]] for v in [*self._vertices] for u in self._vertices[v]]
        return edges

    # @edges.setter
    # def edges(self, graph_dict):
    #     self._edges = [[self.graph_dict[v], u] for v in [*self.graph_dict] for u in self.graph_dict[v]]
    #
    #     self._edges.append()
    #     return self._edges

# class V(Graph):
#
#     def __init__(self, d=1000000, p=None):
#         self._d = d
#         self._p = p
#
#
#     @property
#     def d(self):
#         return self._d
#
#     @d.setter
#     def d(self, weight):
#         self._d = weight
#         return self._d
#
#
#     @property
#     def p(self):
#         return self._p
#
#     @p.setter
#     def p(self, vert):
#         self._p = vert
#         return self._p
#
#
# class Subgraph(object):
#
#     def add_vert(self):
#         pass
#
#     def add_edge(self):
#         pass

# def relax(u, v, w):
#     if v.d > u.d + w[f"{u}, {v}"]:
#         v.d = u.d + w[f"{u}, {v}"]
#         v.p = u

    def relax(self, u, v, w=self.weights):
        if self.d[v] > self.d[u] + w[f"{u}, {v}"]:
            self.d[v] = self.d[v] + w[f"{u}, {v}"]
            self.p[v] = u


def initialize_single_sourse(G, s):
    """ Done """
    for v in [*G.vertices]:
        G.d[v] = 1000000
        G.p[v] = None
    G.d[s] = 0


def dijkstra(G, s):
    initialize_single_sourse(G, s)
    S = []
    Q = Prior_queue([*G.vertices])
    while Q != {}:
        u = Q.heap_extract_min()
        S.append(u)
        for v in G.vertices[u]:
            G.relax(u, v)


if __name__ == "__main__":
    # ==================================== Exam-case =============================================
    import io

    data = [line.split() for line in io.open("task2_dijkstraData.txt").readlines()]
    data = {int(line[0]): [list(map(int, elem.split(","))) for elem in line[1:]] for line in data}

    # d1 = data[1]
    G = Graph(data)
    G.edges