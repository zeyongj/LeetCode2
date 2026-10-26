from collections import deque

class Solution:
    def maxOperations(self, nums):
        nums_queue = deque(nums)

        ret_val = 0

        prev_score = None
        while (len(nums_queue) >= 2):
            num_1 = nums_queue.popleft()
            num_2 = nums_queue.popleft()
            score = num_1 + num_2
            if (prev_score is not None and score != prev_score):
                break
            
            ret_val += 1
            prev_score = score

        return ret_val