class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        n = len(arr)

        # rMin[i] = minimum element from i ... n-1
        rMin = [0] * n
        rMin[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            rMin[i] = min(rMin[i + 1], arr[i])

        leftMax = arr[0]
        chunks = 0

        # Try every possible split.
        for i in range(n - 1):
            leftMax = max(leftMax, arr[i])

            # Every element on the left is <= every element on the right.
            if leftMax <= rMin[i + 1]:
                chunks += 1

        # Last chunk.
        return chunks + 1