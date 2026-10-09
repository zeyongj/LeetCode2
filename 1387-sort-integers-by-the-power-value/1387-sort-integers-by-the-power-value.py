import heapq
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def findPower(x):
            cnt=0
            while x!=1:
                if x%2==0:
                    x//=2
                else:
                    x=x*3+1
                cnt+=1
            return cnt
        heap=[]
        for i in range(lo,hi+1):
            power=findPower(i)
            heap.append((power,i))
        heapq.heapify(heap)
        for i in range(k):
            pow,num=heapq.heappop(heap)
        return num