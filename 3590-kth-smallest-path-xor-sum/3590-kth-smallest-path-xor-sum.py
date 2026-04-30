from sortedcontainers import SortedSet
class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        q_map = defaultdict(list)

        for i, (node, k) in enumerate(queries):
            q_map[node].append((k, i))
        

        def merge(x1, x2):
            if len(x1) < len(x2):
                x2, x1 = x1, x2
            
            x1 |= x2
            return x1

        adj = defaultdict(list)
        ans = [-1] * len(queries)
        for child, par in enumerate(par):
            adj[par].append(child)
        def dfs(curr, p_xor):
            c_xor = p_xor ^ vals[curr]

            main_set = SortedSet()
            main_set.add(c_xor)

            for child in adj[curr]:
                child_set = dfs(child, c_xor)

                main_set = merge(main_set, child_set)
            
            for k, qdex in q_map[curr]:
                if k <= len(main_set):
                    ans[qdex] = main_set[k-1]
            return main_set
        
        dfs(0, 0)
        return ans