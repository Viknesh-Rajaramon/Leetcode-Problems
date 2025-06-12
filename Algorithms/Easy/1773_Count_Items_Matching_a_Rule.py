from imports import *

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        for type_, color, name in items:
            if ruleKey == "type" and type_ == ruleValue:
                result += 1
            elif ruleKey == "color" and color == ruleValue:
                result += 1
            elif ruleKey == "name" and name == ruleValue:
                result += 1
        
        return result
