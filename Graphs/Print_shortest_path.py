#User function Template for python
from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        heap = []
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
        dist = [float('inf') for i in range(n+1)]    
        parent = [i for i in range(n+1)]
        heapq.heappush(heap,(0,1))
        dist[1]=0
     
        while heap:
            dis,node = heapq.heappop(heap)
            for nei in adj[node]:
                adjNode,edgW = nei
                if edgW+dis<dist[adjNode]:
                    dist[adjNode]=edgW+dis
                    heapq.heappush(heap,(dist[adjNode],adjNode))
                    parent[adjNode]= node
        if dist[n]==float('inf'):return [-1]
        #  we have to backtrack from n because we are tracing where we are coming from
        path = []
        node = n
        # this is the back tracking step
        while parent[node]!=node:
            path.append(node)
            node = parent[node]
        # now add the first node
        path.append(1)
        path.reverse()
        return path
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends
