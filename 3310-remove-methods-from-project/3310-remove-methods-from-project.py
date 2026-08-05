class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph =[[] for _ in range(n)]
        for u,v in invocations:
            graph[u].append(v)
        
        sus=[False]*n
        q=deque([k])
        sus[k]=True

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if not sus[nei]:
                    sus[nei]=True
                    q.append(nei)
        for u,v in invocations:
            if not sus[u] and sus[v]:
                return list(range(n))
        return [i for i in range(n) if not sus[i]]