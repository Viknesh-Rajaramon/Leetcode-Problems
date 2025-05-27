from imports import *

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        n = len(logs)
        for i in range(n):
            content = logs[i].split(" ")
            if content[1].isnumeric():
                digit_logs.append(logs[i])
            else:
                letter_logs.append(content)
        
        letter_logs = sorted(letter_logs, key = lambda x: (x[1: ], x[0]))
        result = [" ".join(l) for l in letter_logs] + digit_logs
        return result
