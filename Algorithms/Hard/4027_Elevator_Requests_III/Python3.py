class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        requests.sort(key = lambda x: x[1])
        n = len(requests)
        def min_time(t_i: int, i: int, j: int) -> int:
            t_j = t_i + abs(requests[j][1] - requests[i][1])
            if abs(j-i) == 1:
                return t_j
            
            k = i+1 if j > i else i-1
            t_k = t_i + abs(requests[k][1] - requests[i][1])
            if t_k >= requests[k][0]:
                return min_time(t_k, k, j)
            
            if t_j + abs(requests[k][1] - requests[j][1]) < requests[k][0]:
                t_j = requests[k][0] - abs(requests[k][1] - requests[j][1])
            
            return min(min_time(requests[k][0], k, j), min_time(t_j, j, k))
        
        if n == 1:
            return max(abs(start - requests[0][1]), requests[0][0])

        t0 = max(requests[0][0], abs(requests[0][1] - start), requests[-1][0] - abs(requests[-1][1] - requests[0][1]))
        t1 = max(requests[-1][0], abs(requests[-1][1] - start), requests[0][0] - abs(requests[0][1] - requests[-1][1]))

        return min(min_time(t0, 0, n-1), min_time(t1, n-1, 0))
