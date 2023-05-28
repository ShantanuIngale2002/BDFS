class Graph:
    def __init__(self, V):
        self.V = V
        self.graph=[[] for i in range(V)]
    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, iv):
        visited=[False for i in range(self.V)]
        stack=[]
        stack.append(iv)
        while(len(stack)):
            s = stack.pop()
            if(not visited[s]):
                visited[s]=True
                print(s, end=" ")
            for nodes in self.graph[s]:
                if(not visited[nodes]):
                    stack.append(nodes)
    
    def BFS(self, iv):
        visited=[False for i in range(self.V)]
        queue=[]
        queue.append(iv)
        while(len(queue)):
            q = queue.pop(0)
            if(not visited[q]):
                visited[q]=True
                print(q, end=" ")
            for nodes in self.graph[q]:
                if(not visited[nodes]):
                    queue.append(nodes)

g=Graph(5)

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,1)
g.addEdge(1,4)

g.BFS(0)
