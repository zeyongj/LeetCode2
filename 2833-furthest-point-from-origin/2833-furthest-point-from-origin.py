class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(sum((c=='R')-(c=='L') for c in moves))+moves.count('_')