#https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


#This is a DP question where we need to make the sum equal to target value based on the condition of how many digits can be formed plus how many digit in each place can come
# we can see that there are many base conditions on which we can return our value plus we need to loop over our possible values in each block here k to determine what possible outcomes can come
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def check(n,k,t):
            
            if (n,t) in d:
                return d[(n,t)]
            if n==1 and k>=t:
                d[(n,t)]=1
                return 1
            if n*k<t or n>t or n<=0:
                d[(n,t)]=0
                return 0
            c=0
            for x in range(1,k+1):
                t1=t-x
                if t1>=1:
                    c += check(n-1,k,t1) if (n-1,t1) not in d else d[(n-1,t1)]
            d[(n,t)]=c
            return d[(n,t)]

        d={}

        return check(n,k,target)%(10**9+7)
