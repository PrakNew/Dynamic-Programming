#https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp=[[float('-inf')]*1002 for _ in range(1002)]
        @lru_cache(None)
        def help(i,s):
            if i==M:
                return 0
            if dp[i][s]!=float('-inf'):
                return dp[i][s]
            e=N-(i-s)-1
            op1=multipliers[i]*nums[s]+help(i+1,s+1)
            op2=multipliers[i]*nums[e]+help(i+1,s)
            dp[i][s]=max(op1,op2)
            return dp[i][s]
        M=len(multipliers)
        N=len(nums)
        return help(0,0)
