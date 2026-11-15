class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        p = int(bytearray(arr).translate(b'01' * 128), 2)  # one bit per number, the first number on top: 1 if odd
        s = 1
        while s < len(arr):  # prefix xor by doubling: each bit picks up the parity of everything above it
            p ^= p >> s
            s <<= 1
        odd = p.bit_count()  # odd prefix sums
        return odd * (len(arr) + 1 - odd) % (10**9 + 7)