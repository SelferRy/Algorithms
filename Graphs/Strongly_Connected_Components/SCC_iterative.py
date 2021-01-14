# %%

from collections import deque
import numpy as np
import io

class Graph:

    def __init__(self, data_edges, reverse=False):
        self.reverse = reverse
        if reverse:
            self.edges = [list(map(int, line.split()))[::-1] for line in io.open(data_edges).readlines()]
        else:
            self.edges = [list(map(int, line.split())) for line in io.open(data_edges).readlines()]
        self.graph_size = np.max(self.edges)
        self._explored = {v: False for v in range(1, self.graph_size + 1)}
        self.vertices  = self.fill_vertices()
        self.f = deque()                          # finishing time stack
        self.s = None
        self._leaders = {}
        self.start_order = [*self.vertices][::-1] # assumed vertices in data has sorted order

    def fill_vertices(self):
        self._vertices = {v: [] for v in range(1, self.graph_size + 1)}
        for v1, v2 in self.edges:
            self._vertices[v1].append(v2)
        return self._vertices

    @property
    def explored(self):
        return self._explored

    @explored.setter
    def explored(self, vertex):
        self._explored[vertex] = True

    @property
    def leader(self):
        return self._leaders

    @leader.setter
    def leader(self, s_v):
        s, v = s_v
        if not s in self._leaders:
            self._leaders[s] = []
        if isinstance(v, list):
            self._leaders[s].extend(v)
        else:
            self._leaders[s].append(v)

    @property
    def leader_calc(self):
        self.counter = sorted([len(val) for val in self._leaders.values()], reverse=True)
        return self.counter

# %%

def kosaraju(rev_graph, graph):
    dfs_loop(rev_graph, stack=graph.start_order)
    graph.f = rev_graph.f  # pass finishing-time array from reverse_graph to graph
    dfs_loop(graph, stack=tuple(graph.f))
    return graph.leader_calc


def dfs_loop(graph, stack):
    """ Stack must be reverse vertices (n to 1) for first pass and finishing times (n to 1).
        For second pass stack is f-times array (from last to first). """
    for i in stack:                 # start_order (first pass) or f_times (second)
        if not graph.explored[i]:
            graph.s = i             # get the leader
            dfs(graph, i)


def dfs(graph, i):
    # prev_size = float('inf')
    stack = deque([i])
    while stack:
        v = stack[0]
        if not graph.explored[v]:
            graph.explored[v] = True
            graph.leader = (graph.s, v)
            for j in graph.vertices[v]:
                if not graph.explored[j]:
                    stack.appendleft(j)
        else:
            # kick explored vertex from stack:
            stack.popleft()

            # for get f-times order:
            graph.f.appendleft(v)

    # graph.explored = i              # mark as explored the vertex
    # graph.leader = (graph.s, i)     # collect vertex in leader[s]-list
    # for j in graph.vertices[i]:     # for each arc in (i,j) in G
    #     if not graph.explored[j]:
    #         dfs(graph, j)
    # graph.f.appendleft(i)           # [n, ..., t, ..., 1] - finishing-time stack for second dfs_loop


# %%
if __name__ == "__main__":
    # ================= Multiple test cases ==================
    from get_tests import filter_files

    input_files = filter_files("./test_cases")
    test_cases_dir = "./test_cases/"
    test_paths = [test_cases_dir + file for file in input_files]
    cases = {f"{i}," + str(name.split("/")[-1]): name for i, name in enumerate(test_paths)}
    G = {}
    rev_G = {}
    SCC = {}
    for case in [*cases]:
        G[case] = Graph(cases[case])
        rev_G[case] = Graph(cases[case], reverse=True)
        SCC[case] = kosaraju(rev_G[case], G[case])
        print(f"SCC[{case}] = ", SCC[case])

    # ======================= Single =========================
    ## test = test_cases_dir + input_files[0]
    # test = "./test_cases/input_mostlyCycles_6_16.txt"  #input_mostlyCycles_1_8.txt"
    # G_test = Graph(test)
    # rev_G_test = Graph(test, reverse=True)
    # SCC_test = kosaraju(G_test, rev_G_test)
    # print(SCC_test)

    # ======================== Task ==========================
    # task = "./data_SCC.txt"
    # G = Graph(task)
    # rev_G = Graph(task, reverse=True)
    # SCC = kosaraju(rev_G, G)
    # print(SCC[:5], "This was 5 largest SCC-elements.")