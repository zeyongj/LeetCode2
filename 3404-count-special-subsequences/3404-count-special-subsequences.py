gcds = [[math.gcd(i,j) for i in range(1001)] for j in range(1001)] #precalculate outside of the class
class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        # x1*x3=x2*x4 is equal to: x1/x2 = x4/x3
        n = len(nums)
        ans = 0
        cnt = Counter()
        for x3 in range(4, n):
            x2 = x3-2
            if x2 >= 0: #store ratio x1/x2
                for x1 in range(x2-1):
                    g = gcds[nums[x1]][nums[x2]]
                    cnt[(nums[x1]//g, nums[x2]//g)] += 1
            for x4 in range(x3+2, n): #check ratio x4/3
                g = gcds[nums[x3]][nums[x4]]
                ans += cnt[(nums[x4]//g, nums[x3]//g)]
        return ans