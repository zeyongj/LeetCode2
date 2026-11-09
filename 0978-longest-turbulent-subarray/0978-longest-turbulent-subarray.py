class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        size = len(A)    
        if size == 1:
            return 1
        
        cur_turbu_length = 1 + ( A[0] != A[1] )
        
        max_length = cur_turbu_length
        
        prev_diff = A[1] - A[0]
        
        for i in range(1, size-1):
            post_diff = A[i+1] - A[i]
            
            if prev_diff*post_diff < 0:
                cur_turbu_length += 1
            
            else:
                cur_turbu_length = 1 + (post_diff != 0)
            
            max_length = max( max_length, cur_turbu_length )
            
            prev_diff = post_diff
            
        return max_length