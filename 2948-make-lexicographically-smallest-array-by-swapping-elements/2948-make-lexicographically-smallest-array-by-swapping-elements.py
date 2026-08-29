class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        sorted_nums = sorted(nums)

        group = {}
        groupId = {}
        pos = {}

        id = 1

        # Build groups
        group[id] = [sorted_nums[0]]

        for i in range(1, n):
            if sorted_nums[i] - sorted_nums[i - 1] > limit:
                id += 1

            group.setdefault(id, []).append(sorted_nums[i])

        # Store group id of every value
        id = 1

        for i in range(n):
            if i > 0 and sorted_nums[i] - sorted_nums[i - 1] > limit:
                id += 1

            groupId[sorted_nums[i]] = id

        # Position pointer for each group
        for i in range(1, id + 1):
            pos[i] = 0

        # Rebuild nums using the smallest
        # available value from its group
        for i in range(n):
            grp = groupId[nums[i]]

            nums[i] = group[grp][pos[grp]]
            pos[grp] += 1

        return nums        