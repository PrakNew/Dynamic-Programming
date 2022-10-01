# First of all convert is the function which converts any string to its equivalent number its just an addition
# Secondly we can decode the numbers using 1D DP  where we actually have to see a pattern that
# at a point if the number lies between 1-9 then it is an addition of privious place dp value because if suppose 1,2 is the previous value then if we add suppose 2 then valid cases previously were [(1,2),(12)] and now it becomes [(1,2,2),(12,2)] when added individually
# secondly we need to take the previous element concatinate and check if it lies between 10-26 if so we need to add the i-2 element result to the solution for eg 122 was given till 12 we get [(1,2),(12)] but lets suppose we add 3 now to the end so in that case 23 is checked to be valid and then we get [(1,2,23),(12,23)] so this is also valid so we need to add both the above and below result to produce our answer

#https://leetcode.com/problems/decode-ways/

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

    #level 2 when * is added
    # In order to understand the code you first need to go throught the Decode ways medium level question.
# I am attaching my link to the solution there once you understand that problem you would easily understand this one too.
# Decode Ways
# Click on the above link

# if you have understood the above solution then in below if we use DP we will end up in memory limit exceeded so in order to understand like what needs to be done we just need to modify it to 3 variables as in the below code and use the same logic but instead if * comes first then mulitiply by 9 and similar cases 
# like 1* means 18 and 2* means 6 and ** means 15 on similar basis you can also solve this problem

class Solution:
    def numDecodings(self, s: str) -> int:
        def decodes_ways(s):
            dp = [0]*(10)
            dp[0] = 1

            if s[0]=='*':
                dp[1] = 9
            elif s[0]!='0':
                dp[1] = 1
            two,one=dp[0],dp[1]
            new=0
            for i in range(2,len(s)+1):
                new=0
                # think about 1-1 chars
                if s[i-1] == '*':
                    new = 9*one
                    if s[i-2]=='1':
                        new += 9*two
                    elif s[i-2] == '2':
                        new += 6*two
                    elif s[i-2] == '*':
                        new += (9*two + 6*two)
                elif s[i-1] !='0':
                    new += one

                # think about 2-2 chars
                if s[i-1]!='*':
                    if s[i-2] == '1' or ( s[i-2] == '2' and s[i-1] < '7' ):
                        new += two
                    elif s[i-2]=='*':
                        new += 2*two if s[i-1]<'7' else two
                two,one=one,new
            return new%(10**9+7)
        return decodes_ways(s)
