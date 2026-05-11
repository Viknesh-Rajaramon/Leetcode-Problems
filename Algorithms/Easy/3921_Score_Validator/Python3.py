class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score, counter = 0, 0
        for ele in events:
            if ele == "W":
                counter += 1
                if counter == 10:
                    return [score, counter]
            elif ele == "WD" or ele == "NB":
                score += 1
            else:
                score += int(ele)

        return [score, counter]
