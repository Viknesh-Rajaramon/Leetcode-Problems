from imports import *

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        n = len(beginWord)
        
        all_combo = defaultdict(list)
        for word in wordList:
            for i in range(n):
                all_combo[word[ : i] + "*" + word[i+1:]].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            current_word, level = queue.popleft()

            for i in range(n):
                intermediate_word = current_word[ : i] + "*" + current_word[i+1 : ]
                for word in all_combo[intermediate_word]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        queue.append((word, level+1))
                        visited.add(word)
        
        return 0
