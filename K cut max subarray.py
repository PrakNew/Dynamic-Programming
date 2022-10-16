#https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

'''
array = [6,5,4,3,2,1] , d=2
max([6])+max([5,4,3,2,1])       }
max([6,5])+max([4,3,2,1]        }
.                               }------------minimum of all this
.                               }
.                               }
.
'''

class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        if len(jobs)<d:return -1
        n=len(jobs)
        @cache
        def check(ind,k):
            if k==1:
                try:
                    return max(jobs[ind:])
                except:
                    return inf
            diff=0
            mindiff=float('+inf')
            for x in range(ind,n):
                diff=max(diff,jobs[x])
                mindiff=min(mindiff,diff+check(x+1,k-1))
            return mindiff
        return check(0,d)
    
