class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Step 1: Special case
        if numRows == 1 or numRows >= len(s):
            return s

        # Step 2: Create storage for rows
        rows = []
        for i in range(numRows):
            rows.append("")

        # Step 3: Start from top row
        current_row = 0

        # Step 4: Initially move DOWN
        direction = 1   # +1 means down, -1 means up

        # Step 5: Place each character
        for ch in s:

            # Put character in current row
            rows[current_row] = rows[current_row] + ch

            # If bottom reached → go UP
            if current_row == numRows - 1:
                direction = -1

            # If top reached → go DOWN
            elif current_row == 0:
                direction = 1

            # Move pointer
            current_row = current_row + direction

        # Step 6: Read row by row
        result = ""
        for r in rows:
            result = result + r

        return result
        