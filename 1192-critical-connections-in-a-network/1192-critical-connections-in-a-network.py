class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        visited=[0]*n
        disc=[float('inf')]*n
        low=[float('inf')]*n
        grid=[[] for i in range(n)]
        ans=[]
        for i in connections:
            grid[i[0]].append(i[1])
            grid[i[1]].append(i[0])
        def dfs(node, parent, time):
            visited[node]=1
            time+=1
            disc[node]=time
            low[node]=time
            for i in grid[node]:
                if not visited[i]:
                    dfs(i,node,time)
                    low[node]=min(low[node], low[i])
                    if low[i]>disc[node]:
                        ans.append([node,i])
                elif i!=parent:
                    low[node]=min(low[node],disc[i])
                else:
                    continue
                
        dfs(0,None,0)
        return ans

