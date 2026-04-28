class Solution:
    def __init__(self):
        self.ans = []

        # mapping of digits to letters
        self.keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def solve(self, digits, index, current):
        # if we reached the end
        if index == len(digits):
            self.ans.append(current)
            return

        # current digit
        digit = digits[index]

        # letters for that digit
        letters = self.keypad[digit]

        # try every letter
        for ch in letters:
            self.solve(digits, index + 1, current + ch)

    def letterCombinations(self, digits: str):
        # if input is empty
        if len(digits) == 0:
            return []

        self.solve(digits, 0, "")
        return self.ans