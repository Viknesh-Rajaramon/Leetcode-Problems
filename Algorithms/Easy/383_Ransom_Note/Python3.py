from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)

        for c, count in ransom_counts.items():
            if count > magazine_counts[c]:
                return False

        return True
