class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        result = set()
        for bulb in bulbs:
            if bulb in result:
                result.remove(bulb)
            else:
                result.add(bulb)
        
        return sorted(result)
