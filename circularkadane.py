#https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        if max(arr)<=0:
            return max(arr)
        currmax,maxsum,currmin,minsum=[arr[0]]*4
        for x in range(1,len(arr)):
            currmax=max(currmax+arr[x],arr[x])
            maxsum=max(maxsum,currmax)
            currmin=min(currmin+arr[x],arr[x])
            minsum=min(currmin,minsum)
        return max(maxsum,sum(arr)-minsum)
