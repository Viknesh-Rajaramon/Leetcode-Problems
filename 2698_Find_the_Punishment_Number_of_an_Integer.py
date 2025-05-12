class Solution:
    def canPartition(self, num: int, sum: int, target: int) -> bool:            
            if num == 0:
                return sum == target
            
            if sum > target:
                return False

            return self.canPartition(num//10000, sum+num%10000, target) or self.canPartition(num//1000, sum+num%1000, target) or self.canPartition(num//100, sum+num%100, target) or self.canPartition(num//10, sum+num%10, target)

    def punishmentNumber(self, n: int) -> int:
        sum = 0
        for i in range(1, n+1):
            num = i*i
            if self.canPartition(num, 0, i):
                sum += num
        
        return sum
