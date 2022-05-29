class Graph():
    
    def __init__(self,V,graph= {}):
        self.V= V
        self.graph= graph
        
    def addEdge(self,v,e):
        if v not in self.graph.keys():
            self.graph[v]=[]
            self.graph[v].append(e)
            
            if e not in self.graph.keys():
                self.graph[e]=[]
                self.graph[e].append(v)
        else:
            
            self.graph[v].append(e)
            
    def is_cyclic(self,v,visited,parent):
#         visited = [False]*self.V
        visited[v]= True
        
        for i in self.graph[v]:
            if visited[i]==False:
                if self.is_cyclic(i,visited,v) == True:
                    return True
                
            else:
                if i!= parent:
                    return True
                
        return False
    
    
    def isTree(self):
        
        self.visited = [False]*self.V
        
        if self.is_cyclic(0,self.visited,-1) ==True:
            return False
        
        for i in range(self.V):
            if self.visted[i]==False:
                return False
        
    
g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
    
    
g2.isTree()
