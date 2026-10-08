class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        queries = [tuple(q) for q in queries]
        queries_copy = list(queries)
        rooms.sort()
        queries.sort()
		# stack of rooms with increasing id and decreasing size
        stack = []
        i = 0
        res_cache = {}
        
        def binary_search(min_size):
            low = 0
            high = len(stack) - 1
            while low <= high:
                mid = (low + high + 1) // 2
                if stack[mid][1] < min_size:
                    high = mid - 1
                elif low == mid:
                    return low
                else:
                    low = mid
            return -1
        
		# search the best to the left from prefered position
        for q in queries:
		    # add all rooms to the left from query prefered postion (q[0]) to the stack
            while i < len(rooms) and q[0] >= rooms[i][0]:
			    # discard all rooms that are farther than `rooms[i]` and have smaller size
                while stack and rooms[i][1] >= stack[-1][1]:
                    stack.pop()
                stack.append(rooms[i])
                i += 1
                
			# best room fit to the left from `rooms[i]`
            room_index = binary_search(q[1])
            res_cache[q] = stack[room_index][0] if room_index != -1 else -1
        
        i = 0
        stack = []
        rooms.reverse()
        queries.reverse()
		#  search the best to the right from prefered position
        for q in queries:
		    # add all rooms to the right from query prefered postion `q[0]` to the stack
            while i < len(rooms) and q[0] <= rooms[i][0]:
			    # discard all rooms that are farther than `rooms[i]` and have smaller size
                while stack and rooms[i][1] >= stack[-1][1]:
                    stack.pop()
                stack.append(rooms[i])
                i += 1

			# best room fit to the right from `rooms[i]`
            room_index = binary_search(q[1])
            if room_index != -1 and (res_cache[q] == -1 or q[0] - res_cache[q] > stack[room_index][0] - q[0]):
                res_cache[q] = stack[room_index][0]
                
        return [res_cache[q] for q in queries_copy]