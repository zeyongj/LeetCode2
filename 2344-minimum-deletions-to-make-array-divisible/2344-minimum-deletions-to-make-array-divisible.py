class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        gcd_, mn, ans = gcd(*numsDivide), inf, 0

        mn = min(filter(lambda x: gcd_ % x == 0, nums), default = inf)
        if mn == inf: return -1
       
        return sum(num < mn for num in nums)