from heap_dict import PriorQueue

class Graph(object):

    def __init__(self, graph_dict={}):
        self._vertices = graph_dict
        self._edges = None
        self.d = {}
        self.p = {}
        self._weights = None

    @property
    def vertices(self):
        return self._vertices

    @property
    def weights(self):
        if self._weights == None:
            self._weights = {f"{v}, {u[0]}": u[1] for v in [*self._vertices] for u in self._vertices[v]}
        return self._weights

    @property
    def edges(self):
        if self._edges == None:
            self._edges = self.get_edges()
        return self._edges

    def get_edges(self):
        edges = [[v, u[0]] for v in [*self._vertices] for u in self._vertices[v]]
        return edges


def relax(G, u, v, w, Q):
    """
    Relaxation technique for edge in the graph.

    Note 1 (for use Priority Queue method):
    It can be done with PriorQueue.heap_decrease_key method,
    but need addition indices-array (with positions where Q.d[i] in Q.array).
    It's not efficient for memory used, but in the case can replace Q.build_min_heap() in general function 'dijkstra'
    to Q.heap_decrease_key in sub-function Dijkstra 'relax'.
    But in time-complexity it will faster.

    Note 2 (for use Priority Queue method):
    Another way use Priority Queue method for Dijkstra is create Q with only source vertex (queue's property?).
    Then with help insertion_min_heap insert adjacency vertices to Q (for maintain heap-property).
    That could be done in 'relax' function.

    Parameters
    ----------
    G -- graph
    u -- start-vertex
    v -- finish-vertex
    w -- weights-dict (have weight for edge (u, v))

    Returns
    -------
    None. Just treat G.d[v] and G.p[v] in the graph.
    """
    if G.d[v[0]] > G.d[u] + w[f"{u}, {v[0]}"]:
        G.d[v[0]] = G.d[u] + w[f"{u}, {v[0]}"]
        G.p[v[0]] = u
        Q.min_heap_insert(v[0], G.d[v[0]])


def initialize_single_sourse(G, s):
    """ Done """
    for v in [*G.vertices]:
        G.d[v] = 1000000
        G.p[v] = None
    G.d[s] = 0


Q = 0
def dijkstra(G, s):
    """
    Parameters
    ----------
    G -- graph
    s -- source vertex name

    """
    global Q
    initialize_single_sourse(G, s)
    Q = PriorQueue({s: G.d[s]}, "min")
    Q.heap_size = 0
    while Q.array:
        u = Q.heap_extract_min()
        for v in G.vertices[u]:
            relax(G, u, v, w=G.weights, Q=Q)

if __name__ == "__main__":
    # ==================================== Exam-case =============================================
    import io

    data = [line.split() for line in io.open("task2_dijkstraData.txt").readlines()]
    data = {int(line[0]): [list(map(int, elem.split(","))) for elem in line[1:]] for line in data}

    G = Graph(data)
    distances = dijkstra(G, 1)
    result = [G.d[v] for v in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]]
    print(result)