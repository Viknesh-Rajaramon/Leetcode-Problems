from imports import *

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        result = 0

        for i in range(len(trainers)):
            if players[result] <= trainers[i]:
                result += 1
                
                if result == len(players):
                    break
        
        return result
