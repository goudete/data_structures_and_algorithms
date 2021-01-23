
class Graph:
    """
    Graph class with method for creating
    adjacency list
    """

    def __init__(self, nodes):
        self.nodes = nodes

    def create_directed_adj_list(self):
        """
        Directed graph adj_list using 2d array.
        """
        G = [[] for i in range(len(self.nodes))]

        for node1, node2 in self.nodes:
            G[node1].append(node2)

        return G

    def create_undirected_adj_list(self):
        """
        Undirected graph adj_list using 2d array.
        """
        G = [[] for i in range(len(self.nodes))]

        for node1, node2 in self.nodes:
            G[node1].append(node2)
            G[node2].append(node1)
        return G

class GraphSearchAlgos:
    """
    DFS, BFS and Topological Sort
    """

    def __init__(self, adj_list):
        self.adj_list = adj_list

    def depth_first_search(self, start):
        visited = [False for i in range(len(self.adj_list))]
        visited[start] = True

        def dfs(node):
            print('curr_node:', node)
            for neigh in self.adj_list[node]:
                if not(visited[neigh]):
                    visited[neigh] = True
                    dfs(neigh)

        dfs(start)


    def breadth_first_search(self, start):
        visited = [False for i in range(len(self.adj_list))]
        visited[start] = True
        queue = [start] #how to define starting point

        while queue:
            vertex = queue.pop(0)
            print('curr node:', vertex)
            for neigh in self.adj_list[vertex]:
                if not(visited[neigh]):
                    visited[neigh] = True
                    queue.append(neigh)


    def topological_sort(self, start):
        visited = [False for i in range(len(self.adj_list))]
        # visited[start] = True
        topological_order = []

        def dfs(node):

            for neigh in self.adj_list[node]:
                if not(visited[neigh]):
                    visited[neigh] = True
                    dfs(neigh)
            topological_order.insert(0, node)

        #Traverse all nodes and run dfs
        for i in range(len(visited)):
            if not(visited[i]):
                visited[i] = True
                dfs(i)
        print('topological_order:', topological_order)



#Initialize Graph and create adjacency lists
graph = Graph([[0,1], [1,2], [1,3], [2,3], [3,4]])
directed_adj_list = graph.create_directed_adj_list()
undirected_adj_list = graph.create_undirected_adj_list()

#Initialize Graph search objects
graph_search_directed = GraphSearchAlgos(directed_adj_list)
graph_search_undirected = GraphSearchAlgos(undirected_adj_list)

#Run dfs on directed and undirected graphs
print('DFS:')
print('Directed Graph:')
graph_search_directed.depth_first_search(3)
print('----------')
print('Undirected Graph')
graph_search_undirected.depth_first_search(3)

print(' ')

#Run bfs on directed and undirected graphs
print('BFS:')
print('Directed Graph:')
graph_search_directed.breadth_first_search(3)
print('----------')
print('Undirected Graph')
graph_search_undirected.breadth_first_search(3)

print(' ')

#Topological sort on Directed Acyclic Graph (DAG)
print('Topological Sort')
graph_search_directed.topological_sort(4)

print(' ')
