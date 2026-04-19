class Solution:
    def reverseWords(self, s: str) -> str:
        def vowel_count(word: str) -> int:
            count = 0
            for c in word:
                if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
                    count += 1

            return count

        result = s.split(" ")
        count = vowel_count(result[0])
        for i in range(1, len(result)):
            if vowel_count(result[i]) == count:
                result[i] = result[i][::-1]

        return " ".join(result)
