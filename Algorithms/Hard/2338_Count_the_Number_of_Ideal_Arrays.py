mod = 10**9 + 7
max_n = 10**4 + 10
max_p = 15

sieve = [0] * max_n

for i in range(2, max_n):
    if not sieve[i]:
        for j in range(i, max_n, i):
            sieve[j] = i

ps = [[] for _ in range(max_n)]

for i in range(2, max_n):
    x = i
    while x > 1:
        p = sieve[x]
        count = 0
        while not (x % p):
            x //= p
            count += 1
        
        ps[i].append(count)

c = [[0] * (max_p + 1) for _ in range(max_n + max_p)]
c[0][0] = 1
for i in range(max_n + max_p):
    c[i][0] = 1
    for j in range(1, min(i, max_p) + 1):
        c[i][j] = (c[i-1][j] + c[i-1][j-1]) % mod

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        result = 0
        for x in range(1, maxValue + 1):
            mul = 1
            for p in ps[x]:
                mul = (mul * c[n + p - 1][p]) % mod
            result = (result + mul) % mod
        
        return result
