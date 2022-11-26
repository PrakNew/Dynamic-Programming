# Start time and end time are there and the maximum profit needs to be founded without any overlap 
1235. Maximum Profit in Job Scheduling  https://leetcode.com/problems/maximum-profit-in-job-scheduling/
https://www.youtube.com/watch?v=cr6Ip0J9izc

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        dp = [[0,0]]                                            #   e     s     p     dp
                                                                #  ––-–  ––-–  ––-–  ––––––––––––––––-–
        f = lambda x: dp[bisect_left(dp,[x+1])-1][1]            #    3     1    20   [[0,0],[3,20]]
                                                                #    5     2    20   [[0,0],[3,20],[5,20]]
        for e, s, p in sorted(zip(endTime,startTime, profit)):  #    6     4    70   [[0,0],[3,20],[5,20],[6,90]]
                                                                #    9     6    60   [[0,0],[3,20],[5,20],[6,90],[9,150]]
            dp.append([e, max(f(e),f(s)+p)])                    #   10     3   100   [[0,0],[3,20],[5,20],[6,90],[9,150],[10,150]]
                                                                #                                                             |          
        return dp[-1][1]                                        #                                                           answer
