from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = defaultdict(list)
        
        # Build graph
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if color[i] != 0:
                continue
            
            queue = deque([i])
            color[i] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        
        return True
