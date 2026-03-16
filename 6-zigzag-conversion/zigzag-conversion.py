class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = []
        for i in range(numRows):
            rows.append("")

        current_row = 0

        direction = 1   

        for ch in s:

            rows[current_row] = rows[current_row] + ch

            if current_row == numRows - 1:
                direction = -1

            elif current_row == 0:
                direction = 1

            current_row = current_row + direction

        result = ""
        for r in rows:
            result = result + r

        return result
        