class Solution:
    def smallestTrimmedNumbers(
        self, nums: List[str], queries: List[List[int]]
    ) -> List[int]:
        result = []

        for k, trim in queries:
            new_nums = [num[-trim:] for num in nums]

            # Sort indices based on their trimmed values
            get_index = sorted(
                range(len(new_nums)),
                key=lambda x: new_nums[x]
            )

            result.append(get_index[k - 1])

        return result