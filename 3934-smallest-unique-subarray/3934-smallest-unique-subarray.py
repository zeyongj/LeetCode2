import numpy as np


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        names = [np.unique(nums, return_inverse=True)[1]]  # names[k][i] is equal for equal windows nums[i:i + 2**k]
        for k in range(n.bit_length() - 1):  # blocks of 2, 4, 8, ... while they fit
            if 1 in np.bincount(names[k]):  # some block is unique already: longer ones are not needed
                break
            pairs = names[k][:-2 ** k] * n + names[k][2 ** k:]  # two halves as one number
            names.append(np.unique(pairs, return_inverse=True)[1])

        def found(length):  # is some window of this length unique?
            k = length.bit_length() - 1  # its first 2**k elements and its last 2**k cover it
            pairs = names[k][:n - length + 1] * n + names[k][length - 2 ** k:]
            return 1 in np.unique(pairs, return_counts=True)[1]

        return bisect_left(range(1, min(2 ** len(names), n)), True, key=found) + 1