class Solution(object):
    def dfs(self,node,adj,vis,pathVis,check):
        vis[node]=1
        pathVis[node]=1
        check[node]=0
        for x in adj[node]:
            if vis[x]!=1:
                if self.dfs(x,adj,vis,pathVis,check)==True:
                    return True
            elif pathVis[x]==1:
                return True
        check[node]=1
        pathVis[node]=0
        return False
    def eventualSafeNodes(self, graph):
        n=len(graph)
        vis=[0]*n
        pathVis=[0]*n
        check=[0]*n
        safeNodes=[]
        for i in range(n):
            if vis[i]!=1:
                self.dfs(i,graph,vis,pathVis,check)
        for i in range(n):
            if check[i]==1:
                safeNodes.append(i)
        return safeNodes

  # Using Kahns Algorithm
  
#     class Queue:
#     def __init__(self):
#         self.q=[]
#         self.front=-1
#     def push(self,x):
#         if self.front==-1:
#             self.front=0
#         self.q.append(x)
#     def pop(self):
#         if len(self.q)==0:
#             return -1
#         x=self.q[self.front]
#         self.front+=1
#         if self.front==len(self.q):
#             self.front=-1
#             self.q=[]
#         return x
#     def size(self):
#         if self.front==-1:
#             return 0
#         return len(self.q)-self.front
# class Solution(object):
#     def eventualSafeNodes(self, graph):
#         n=len(graph)
#         adjRev=[[0] for i in range(n)]
#         inDegree=[0]*n
#         for i in range(n):
#             for x in graph[i]:
#                 adjRev[x].append(i)
#                 inDegree[i]+=1
#         q=Queue()
#         for i in range(n):
#             if inDegree==0:
#                 q.push()
#         ans=[]
#         while q.size()>0:
#             node=q.front
#             ans.append(node)
#             for x in adjRev[node]:
#                 inDegree-=1
#                 if inDegree[x]==0:
#                     q.push(x)
#         return ans