#https://leetcode.com/problems/longest-common-subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[0]*(m+1) for _ in range(n)]
        for x in range(n):
            for y in range(m):
                if text1[x]==text2[y]:
                    dp[x][y]=dp[x-1][y-1]+1
                else:
                    dp[x][y]=max(dp[x-1][y],dp[x][y-1])
        return dp[n-1][m-1]






#import sys
#sys.setrecursionlimit(1000000)
def lcs_length(x,y,m,n):
	c=[list([0]*(n+1))[:] for x in range(m+2)]
	#b=[list([0]*(n+1))[:] for x in range(m+2)]
	for i in range(1,m+1):
		for j in range(1,n+1):
			if x[i]==y[j]:
				c[i][j]=c[i-1][j-1]+1
				#b[i][j]="upleft"
			elif c[i-1][j]>=c[i][j-1]:
				c[i][j]=c[i-1][j]
				#b[i][j]="up"
			else:
				c[i][j]=c[i][j-1]
				#b[i][j]="left"
	return c
q3=input()
q4=input()
q1="0"+q3
q2="0"+q4
a=lcs_length(q1,q2,len(q1)-1,len(q2)-1)
#p=""
print(a[len(q1)-1][len(q2)-1])
'''print(b)
c=0
def print_lcs(b,x,i,j):
	#global p
	global c
	#p=""
	if i==0 or j==0:
		return
	if b[i][j]=="upleft":
		print_lcs(b,x,i-1,j-1)
		#print(x[i-1])
		c=c+1
		#p=p+x[i-1]
	elif b[i][j]=="up":
		print_lcs(b,x,i-1,j)
	else:
		print_lcs(b,x,i,j-1)
print_lcs(b,q3,len(q1)-1,len(q2)-1)
#print(p)
print(c)'''
