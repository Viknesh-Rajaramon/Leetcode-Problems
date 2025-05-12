class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for word in s.split(" ")[::-1]:
            if word == "":
                continue
            
            return len(word)

        return 0
