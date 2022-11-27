

from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, A):
        n = len(A)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    res += dp[j][diff]
        
        return res
