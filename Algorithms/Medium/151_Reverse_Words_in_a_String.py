class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = [word for word in words if word != ""]

        return " ".join(word for word in words[::-1])
