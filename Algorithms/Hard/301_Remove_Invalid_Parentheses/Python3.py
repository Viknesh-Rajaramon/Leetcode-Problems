class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = []
        def helper(s: str, left: int, right: int, open_p: str, close_p: str) -> None:
            count = 0
            while right < len(s):
                if s[right] == open_p:
                    count += 1
                elif s[right] == close_p:
                    count -= 1

                if count < 0:
                    break

                right += 1

            if count < 0:
                while left <= right:
                    if (s[left] == close_p) and (left == 0 or s[left] != s[left-1]):
                        helper(s[ : left] + s[left+1 : ], left, right, open_p, close_p)
                    
                    left += 1
            elif count > 0:
                helper(s[ : : -1], 0, 0, close_p, open_p)
            else:
                if open_p == '(':
                    result.append(s)
                else:
                    result.append(s[ : : -1])

        helper(s, 0, 0, '(', ')')
        return result
