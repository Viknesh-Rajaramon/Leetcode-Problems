class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        result, old_temp = [], [nums]
        for bit in range(14, -1, -1):
            mask, count, splitting, new_temp = 1 << bit, 0, True, []
            for section in old_temp:
                if splitting:
                    section_0, section_1 = [], []
                    for num in section:
                        if num & mask:
                            section_1.append(num)
                        else:
                            section_0.append(num)
                    
                    if len(section_1) > 0:
                        count += len(section_1)
                        new_temp.append(section_1)
                    
                    if len(section_0) > 0:
                        splitting = False
                        new_temp.append(section_0)
                else:
                    new_temp.append(section)
            
            result.append(count)
            old_temp = new_temp

        return result
