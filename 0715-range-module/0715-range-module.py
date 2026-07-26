class RangeModule:

    def __init__(self):
        self.intervals = [] # sorted

    def addRange(self, left: int, right: int) -> None:
        res = [] 
        inserted = False # [left, right] inserted or not

        for curLeft, curRight in self.intervals:
            if curRight < left:
                res.append([curLeft, curRight])
            elif curLeft > right:
                if not inserted:
                    res.append([left, right])
                    inserted = True
                res.append([curLeft, curRight])
            else:
                left = min(left, curLeft)
                right = max(right, curRight)
        
        if not inserted:
            res.append([left, right])
        self.intervals = res

    def queryRange(self, left: int, right: int) -> bool:
        for curLeft, curRight in self.intervals:
            # Case: [curLeft, [left, right], curRight] -> must be included
            if curLeft <= left and right <= curRight:
                return True
            # Case: [left, [curLeft, curRight], right] -> could not be included
            # Case: [left, curLeft, right, curRight] -> could not be included
            if left < curLeft:
                return False                
        return False

    def removeRange(self, left: int, right: int) -> None:
        res = []
        for curLeft, curRight in self.intervals:
            # No overlap, just add
            if curRight <= left or curLeft >= right:
                res.append([curLeft, curRight])
            # Overlap, update intervals
            else:
                # Case: [curLeft, left]
                if curLeft < left:
                    res.append([curLeft, left])
                # Case: [right, curRight]
                if curRight > right:
                    res.append([right, curRight])
        self.intervals = res
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)