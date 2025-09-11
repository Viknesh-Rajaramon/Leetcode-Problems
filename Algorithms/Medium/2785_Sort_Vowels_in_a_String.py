class Solution:
    def sortVowels(self, s: str) -> str:
        result = []
        vowels = set('AEIOUaeiou')
        arr = sorted([c for c in s if c in vowels])

        i = 0
        for c in s:
            if c in vowels:
                result.append(arr[i])
                i += 1
            else:
                result.append(c)

        return "".join(result)
