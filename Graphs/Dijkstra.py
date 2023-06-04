from collections import deque
import heapq 
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        heap = []
        heapq.heappush(heap,(0,S))
        dist = [float('inf') for i in range(V)]
        dist[S]=0
        while heap:
            dis,node = heapq.heappop(heap)
            for i in adj[node]:
                adjNode = i[0]
                edgeWgt = i[1]
                if edgeWgt+dis<dist[adjNode]:
                    dist[adjNode]=edgeWgt+dis
                    heapq.heappush(heap,(dist[adjNode],adjNode))
        return dist            
                            
        
        
        
#  ________________________________________________________________


from sortedcontainers import SortedSet

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        s = SortedSet()
        dist = [float('inf') for i in range(V)]
        # dis,node
        s.add((0,S))
        dist[S]=0
        while s:
            dis,node = s[0]
            s.remove((dis,node))
            for i in adj[node]:
                adjNode,edgW = i
                if dis+edgW<dist[adjNode]:
                    #erase if existed in set
                    if dist[adjNode]!=float('inf'):
                        # means it has been visited and has more weight 
                        # so we will remove it from the set before inserting
                        s.remove((dist[adjNode],adjNode))
                    dist[adjNode]=dis+edgW
                    s.add((dist[adjNode],adjNode))
        return dist            
              
                            
