import numpy as np

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # 1. Transform letters to numbers (Frequency Analysis)
        _, counts = np.unique(list(word), return_counts=True)
        M = len(counts)
        
        # 2. Create an M x M matrix of the current frequency signal
        # Each row will represent a 'Trial' removal
        field = np.tile(counts, (M, 1))
        
        # 3. Apply the 'Unit Pulse' removal to the diagonal
        # This removes 1 from each character once per trial row
        np.fill_diagonal(field, field.diagonal() - 1)
        
        # 4. Uniformity Check across the field
        # For each row, we need all non-zero elements to be equal.
        # This is the tricky part to vectorize perfectly:
        def is_uniform(row):
            active = row[row > 0]
            return bool(np.all(active == active[0])) if len(active) > 0 else False

        # Vectorized check using a mask to handle zeros
        # We find the max of each row and compare it to the sum/count
        # If (Max * Count) == Sum, all non-zero elements are equal.
        max_vals = np.max(field, axis=1)
        row_sums = np.sum(field, axis=1)
        row_counts = np.sum(field > 0, axis=1)
        
        # Avoid division by zero: a row is valid if all non-zeros are the same
        # Potential Case: row_counts can't be 0 because we only removed 1 letter
        success_mask = (max_vals * row_counts == row_sums)
        
        return bool(np.any(success_mask))        