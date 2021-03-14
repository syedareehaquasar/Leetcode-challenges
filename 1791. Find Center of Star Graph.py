from collections import defaultdict 

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            e1, e2 = edge[0], edge[1]
            graph[e1].append(e2)
            graph[e2].append(e1)
        l = 0
        for node in graph:
            if len(graph[node]) == (len(edges)):
                return node
            if len(graph[node]) > l:
                n = node
                l = len(graph[node])
        return n
            
