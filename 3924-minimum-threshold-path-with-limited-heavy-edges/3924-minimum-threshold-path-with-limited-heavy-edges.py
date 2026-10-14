class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        maxy=0
        graph=defaultdict(list)
        for a,b,c in edges:
            graph[a].append((b,c))
            graph[b].append((a,c))
            maxy=max(maxy,c)
        def dhunuku_dhunuku_algo(val):
            distance=[float('inf')]*n
            distance[source]=0
            heap=[(0,source)]
            while(heap):
                cst,u=heappop(heap)
                if distance[u]<cst:
                    continue
                for v,c in graph[u]:
                    c=1 if c>val else 0
                    if cst+c<distance[v]:
                        heappush(heap,(cst+c,v))
                        distance[v]=cst+c
            return distance[target]<=k
        low,high=0,maxy
        res=-1
        while(low<=high):
            mid=low+((high-low)//2)
            if dhunuku_dhunuku_algo(mid):
                high=mid-1
                res=mid
            else:
                low=mid+1
        return res
