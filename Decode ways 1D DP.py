# First of all convert is the function which converts any string to its equivalent number its just an addition
# Secondly we can decode the numbers using 1D DP  where we actually have to see a pattern that
# at a point if the number lies between 1-9 then it is an addition of privious place dp value because if suppose 1,2 is the previous value then if we add suppose 2 then valid cases previously were [(1,2),(12)] and now it becomes [(1,2,2),(12,2)] when added individually
# secondly we need to take the previous element concatinate and check if it lies between 10-26 if so we need to add the i-2 element result to the solution for eg 122 was given till 12 we get [(1,2),(12)] but lets suppose we add 3 now to the end so in that case 23 is checked to be valid and then we get [(1,2,23),(12,23)] so this is also valid so we need to add both the above and below result to produce our answer


class Solution:
    def numDecodings(self, s: str) -> int:
        def convert(s):
            l = list('abcdefghijklmnopqrstuvwxyz')
            d = {x: c for c, x in enumerate(l, start=1)}
            q = sum((26 ** (c - 1)) * d[s[x]]
                    for c, x in enumerate(range(len(s) - 1, -1, -1), start=1))
            return q

        if not s or s[0] == '0':
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != 0 else 0

        for x in range(2, len(s)+1):
            if 1 <= int(s[x-1]) <= 9:
                dp[x] += dp[x-1]
            if 10 <= int(s[x-2:x]) <= 26:
                dp[x] += dp[x-2]
        return dp[len(s)]
