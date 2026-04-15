class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        total_rooms = len(rooms)
        visited = {0}
        keys = rooms[0]
        count = self.findPath(keys, visited, rooms)
        if count == total_rooms:
            return True
        else: return False
    
    def findPath(self, keys, visited, rooms):
        while len(keys) > 0:
            room = keys.pop(0)
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    if key not in visited:
                        keys.append(key)
        return len(visited)
