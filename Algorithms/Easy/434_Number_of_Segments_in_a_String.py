class Solution:
    def countSegments(self, s: str) -> int:
        stack = []
        word = []
        for c in s:
            if c == " ":
                if word:
                    stack.append(word)
                word = []
            else:
                word.append(c)

        if word:
            stack.append(word)
            
        return len(stack)
