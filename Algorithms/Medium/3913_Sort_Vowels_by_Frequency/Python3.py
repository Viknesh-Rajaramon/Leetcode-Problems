class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiou")
        counts = {c: s.count(c) for c in vowels if s.count(c) > 0}
        position = {c: s.index(c) for c in vowels if c in counts}
        if len(position) == 0:
            return s
        
        counts = sorted(counts.items(), key = lambda x: (x[1], -position.get(x[0])))
        result = list(s)
        letter, count = counts.pop()
        for i, c in enumerate(s):
            if c not in vowels:
                continue
            
            result[i] = letter
            count -= 1
            if count == 0 and counts:
                letter, count = counts.pop()

        return "".join(result)
