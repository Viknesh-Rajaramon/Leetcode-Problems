from collections import defaultdict

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        result = []
        def generate_beautiful(i: int, m: int, curr_num: int, count: defaultdict):
            if i == m:
                for key in count.keys():
                    if count[key] == 0:
                        continue
                    elif count[key] != key:
                        return
                
                result.append(curr_num)
                return
            
            for d in range(1, m+1):
                if count[d] == d or count[d] + m - i < d:
                    continue
                
                count[d] += 1
                generate_beautiful(i+1, m, curr_num*10 + d, count)
                count[d] -= 1
        
        generate_beautiful(0, len(str(n)), 0, defaultdict(int))
        if result[-1] <= n:
            result = []
            generate_beautiful(0, len(str(n))+1, 0, defaultdict(int))

        for num in result:
            if num > n:
                return num
