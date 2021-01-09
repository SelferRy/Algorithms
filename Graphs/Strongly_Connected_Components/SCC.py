# %%

from collections import deque
import numpy as np
import io

file = "./data_SCC.txt"
test_file = "./data_SCC_test.txt"


class Graph:

    def __init__(self, data_edges, reverse=False):
        self.reverse = reverse
        if reverse:
            self.edges = [list(map(int, line.split())) for line in io.open(data_edges).readlines()]
        else:
            self.edges = [list(map(int, line.split())) for line in io.open(data_edges).readlines()]
        self.graph_size = np.max(self.edges)
        # =====================================
        self.vertices = self.vertices()
        # =====================================
        self._explored = {v: False for v in [*self.vertices]}
        self.t = 0  # time
        self.f = deque()  # finishing time
        self.s = None
        self._leaders = {}  # self.empty_vert.copy()
        # self.counter = {}
        self.start_order = [n for n in range(self.graph_size, 0, -1)]

    # @property
    # def graph_size(self):
    #     print("graph_size =", np.max(self.edges))
    #     return np.max(self.edges)

    @property
    def empty_vert(self):
        self._empty_vert = {v: [] for v in range(1, self.graph_size + 1)}  #
        return self._empty_vert

    # @property
    def vertices(self):
        self._vertices = self.empty_vert.copy()
        if self.reverse:
            for v1, v2 in self.edges:
                self._vertices[v2].append(v1)
        else:
            for v1, v2 in self.edges:
                self._vertices[v1].append(v2)
        return self._vertices

    @property
    def explored(self):
        return self._explored

    @explored.setter
    def explored(self, tuple_val):
        if tuple_val == "reset":
            self._explored = {v: False for v in [*self.vertices]}
        else:
            i, val = tuple_val
            self._explored[i] = val

    @property
    def leader(self):
        return self._leaders

    @leader.setter
    def leader(self, s_v):
        s, v = s_v
        if not s in self._leaders:
            self._leaders[s] = []
        self._leaders[s].append(v)

    @property
    def leader_calc(self):
        self.counter = sorted([len(val) for val in self._leaders.values()], reverse=True)
        # print("Count leaders:", self.counter)
        return self.counter

# %%

def kosaraju(rev_graph, graph):
    dfs_loop(rev_graph, stack=graph.start_order)
    graph.f = rev_graph.f  # pass finishing time from reverse_graph to graph
    dfs_loop(graph, stack=tuple(graph.f))
    return graph.leader_calc


def dfs_loop(graph, stack):
    """ stack must be reverse vertices (n to 1) for first pass and finishing times (n to 1)"""
    for i in stack:  # start_order (first pass) or f_times (second)
        if not graph.explored[i]:
            graph.s = i  # get the leader
            dfs(graph, i)
            # graph.counter[i] = len(graph.leaders[i])    # calc len the leader's list == how big the SCC


def dfs(graph, i):
    graph.explored = (i, True)  # mark as explored the vertex
    graph.leader = (graph.s, i)  # collect vertex in leader[s]-list
    for j in graph.vertices[i]: # graph.edges:  # for each arc in (i,j) in G
        if not graph.explored[j]:
            dfs(graph, j)
    graph.t += 1  # increment t
    graph.f.appendleft(graph.t)  # [n, ..., t, ..., 1] - finishing time stack for second dfs_loop


# %%
if __name__ == "__main__":
    # ==================== Test cases =====================
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
        SCC[case] = kosaraju(G[case], rev_G[case])
        print(f"SCC[{case}] = ", SCC[case])

    # =================== Single =======================
    # test = test_cases_dir + input_files[0]
    # test = "./test_cases/input_mostlyCycles_1_8.txt"
    # G_test = Graph(test)
    # rev_G_test = Graph(test, reverse=True)
    # SCC_test = kosaraju(G_test, rev_G_test)
    # print(SCC_test)

    # ======================== Task ===========================
    # import sys, threading
    # sys.setrecursionlimit(800000)
    # threading.stack_size(67108864)  # 67108864
    #
    # task = "./data_SCC.txt"
    # G = Graph(task)
    # rev_G = Graph(task, reverse=True)
    # def main():
    #
    #     global G
    #     global rev_G
    #     SCC = kosaraju(G, rev_G)
    #     print(SCC, "This was SCC")
    #     return G, rev_G, SCC
    #
    # # G, rev_G, SCC = main()
    # thread = threading.Thread(target=main)
    # thread.start()