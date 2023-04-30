class Solution:
    def climbStairs(self, n: int) -> int:
        # dp solution tabulation 
        step1 = 0
        step2 = 1
        for i in range(n):
            curr = step1+step2 
            step1 = step2
            step2 = curr 
        return step2 
