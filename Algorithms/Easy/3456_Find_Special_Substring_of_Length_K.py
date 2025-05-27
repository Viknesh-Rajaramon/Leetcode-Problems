class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        stack = []
        letter = s[0]

        stack.append(letter)
        
        for i in range(1, len(s)):
            if s[i] == letter:
                stack.append(s[i])
            elif len(stack) == k:
                    return True
            else:
                stack.clear()
                stack.append(s[i])
                letter = s[i]

        if len(stack) == k:
            return True

        return False
