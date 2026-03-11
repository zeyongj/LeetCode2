class Solution:
    def minimumOperations(self, s: str) -> int:
        min_operations = float('inf') # Initialize a variable to store the minimum operations.
        
        c = list(s) # Convert the input string to a list of characters for easier traversal.

        for i in range(len(c) - 1, -1, -1):
            if c[i] == '5':
                for j in range(i - 1, -1, -1):
                    if c[j] == '2' or c[j] == '7':
                        f = i - j - 1 # Calculate the number of characters between i and j exclusive.
                        l = len(c) - 1 - i # Calculate the number of characters from i to the end of the string.

                        min_operations = min(f + l, min_operations) # Update the minimum operations with the minimum of the current value and f + l.
                        break # Exit the inner loop since we found a valid pair.

            if c[i] == '0':
                for j in range(i - 1, -1, -1):
                    if c[j] == '0' or c[j] == '5':
                        f = i - j - 1 # Calculate the number of characters between i and j exclusive.
                        l = len(c) - 1 - i # Calculate the number of characters from i to the end of the string.

                        min_operations = min(f + l, min_operations) # Update the minimum operations with the minimum of the current value and f + l.
                        break # Exit the inner loop since we found a valid pair.

        if min_operations == float('inf'):
            # If no valid pairs of '5' or '0' are found, check if the string contains '0'.
            # If it does, return the length of the string minus 1, otherwise, return the length of the string.
            if '0' in s:
                return len(s) - 1
            else:
                return len(s)

        return min_operations # Return the minimum operations.