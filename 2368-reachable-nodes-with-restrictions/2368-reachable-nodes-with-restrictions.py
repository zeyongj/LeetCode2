class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        seen = set(restricted)
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        dq = deque([0])
        while dq:
            node = dq.popleft()
            seen.add(node)
            for kid in g[node]:
                if kid not in seen:
                    seen.add(kid)
                    dq.append(kid)
        return len(seen) - len(restricted) 