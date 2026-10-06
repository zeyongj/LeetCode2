import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center        

    def randPoint(self) -> List[float]:
        # 1. Coordinate Mapping (Low-Discrepancy Flow)
        # We transform a uniform 1D 'flow' into a 2D area-consistent distribution
        r = self.radius * math.sqrt(random.random())
        theta = 2 * math.pi * random.random()
        
        # 2. Coordinate Projection
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()