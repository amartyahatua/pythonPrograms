from collections import  defaultdict
import  numpy as np
class Graph:
    def __init__(self, vertex):
        self.graph = defaultdict(list)
        self.V = vertex
        self.tc = np.zeros((self.V, self.V))
        self.node = 0


    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtils(self,v,visited):
        visited[v] = True
        self.tc[self.node][v] = 1
        #print(v)

        for i in self.graph[v]:
            if (visited[i] == False):
                self.DFSUtils(i,visited)



    def DFS(self,s):
        visited = [False]*(len(self.graph))
        self.DFSUtils(s,visited)

    def transitiveClosure(self):
        for i in self.graph:
            self.tc[i][i] = 1
            self.node = i
            self.DFS(i)

        print(self.tc)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


print ("Transitive closure matrix is")
g.transitiveClosure();