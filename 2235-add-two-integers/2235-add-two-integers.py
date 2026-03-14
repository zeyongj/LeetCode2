class Solution:
    def sum(self, num1: int, num2: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while num2 != 0:
            num1, num2 = (num1 ^ num2) & mask, ((num1 & num2) << 1) & mask
        return num1 if num1 <= MAX else ~(num1 ^ mask)