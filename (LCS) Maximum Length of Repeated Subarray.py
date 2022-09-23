#https://leetcode.com/problems/maximum-length-of-repeated-subarray/
#Largest common subarray

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m=len(nums1),len(nums2)
        dp=[[0]*(m+1) for _ in range(n+1) ]
        ma=0
        for x in range(n):
            for y in range(m):
                if nums1[x]==nums2[y]:
                    dp[x][y]=dp[x-1][y-1]+1
                    ma=max(ma,dp[x][y])
        return ma
 
