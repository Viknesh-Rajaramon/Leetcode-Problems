from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        pre, suf, max_len = [0] * (4*n), [0] * (4*n), [0] * (4*n)
        left_char, right_char = [""] * (4*n), [""] * (4*n)

        def push_up(u: int, l: int, r: int) -> None:
            m = (l+r) >> 1
            left_len, right_len, left, right = m-l+1, r-m, u << 1, u << 1 | 1
            left_char[u], right_char[u] = left_char[left], right_char[right]
            pre[u], suf[u] = pre[left], suf[right]

            if pre[left] == left_len and right_char[left] == left_char[right]:
                pre[u] = pre[left] + pre[right]
            
            if suf[right] == right_len and right_char[left] == left_char[right]:
                suf[u] = suf[right] + suf[left]
            
            max_len[u] = max(max_len[left], max_len[right])
            if right_char[left] == left_char[right]:
                max_len[u] = max(max_len[u], suf[left] + pre[right])

        def build(u: int, l: int, r: int) -> None:
            if l == r:
                pre[u], suf[u], max_len[u], left_char[u], right_char[u] = 1, 1, 1, s[l], s[l]
                return
            
            m = (l+r) >> 1
            build(u << 1, l, m)
            build(u << 1 | 1, m+1, r)
            push_up(u, l, r)

        def update(u: int, l: int, r: int, pos: int, ch: str) -> None:
            if l == r:
                left_char[u], right_char[u] = ch, ch
                return
            
            m = (l+r) >> 1
            if pos <= m:
                update(u << 1, l, m, pos, ch)
            else:
                update(u << 1 | 1, m+1, r, pos, ch)
            
            push_up(u, l, r)
        
        build(1, 0, n-1)
        result, k = [], len(queryIndices)
        for i in range(k):
            update(1, 0, n-1, queryIndices[i], queryCharacters[i])
            result.append(max_len[1])

        return result
