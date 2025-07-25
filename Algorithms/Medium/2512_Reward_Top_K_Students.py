from imports import *

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        feedback = {}
        for word in positive_feedback:
            feedback[word] = 3
            
        for word in negative_feedback:
            feedback[word] = -1
        
        scores = defaultdict(list)
        for i in range(len(student_id)):
            score = 0
            for word in report[i].split(" "):
                if word in feedback:
                    score += feedback[word]
            
            scores[score].append(student_id[i])
        
        result = []
        for score in sorted(scores.keys(), reverse = True):
            for student in sorted(scores[score]):
                result.append(student)
                if len(result) == k:
                    return result
        
        return result
