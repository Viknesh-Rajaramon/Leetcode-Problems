class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        result, col = [], len(encodedText) // rows
        for i in range(col):
            r, c = 0, i
            while r < rows and c < col:
                result.append(encodedText[r*col + c])
                r += 1
                c += 1

        return "".join(result).rstrip()
