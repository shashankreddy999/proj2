def algo5_helper(i,j,tt,dp):
    if dp[i][j]!=-1:
        return dp[i][j]
    if i == 0 or j == 0:
        dp[i][j] = 0
    elif tt[i-1][j-1]==0 or tt[i-1][j]==0 or tt[i][j-1]==0:
        dp[i][j]=2
    else:
        minel=min(algo5_helper(i-1,j-1,tt,dp),algo5_helper(i-1,j,tt,dp),algo5_helper(i,j-1,tt,dp))
        a=0
        b=0
        
        if algo5_helper(i-1,j-1,tt,dp)== minel:
            a=i-1
            b=j-1
            if tt[a-dp[a][b]+1][b]==1 and tt[a][b-dp[a][b]+1]==1:
                dp[i][j]=algo5_helper(i-1,j-1,tt,dp)+1
            else:
                dp[i][j]=2
        elif algo5_helper(i-1,j,tt,dp)== minel:
            a=i-1
            b=j
            if tt[a][j-dp[a][b]+1]==1:
                dp[i][j]=algo5_helper(i-1,j,tt,dp)+1
            else: 
                dp[i][j]=2
        elif algo5_helper(i,j-1,tt,dp)== minel:
            a=i
            b=j-1
            if tt[i-dp[a][b]+1][b]==1:
                dp[i][j]=algo5_helper(i,j-1,tt,dp)+1
            else:
                dp[i][j]=2
    return dp[i][j]

def task5a(arr,h):
    m = len(arr)
    n = len(arr[0])
    dp = [[-1] * n for i in range(m)]
    max_size = 0
    res_x,res_y=0,0
    tt= [[0] * n for i in range(m)]

    for i in range(0,m):
        for j in range(0,n):
            if arr[i][j]>=h:
                tt[i][j]=1 
            else: 
                tt[i][j]=0
  
    for i in range(0,m):
        dp[i][0]=1
        dp[i][1]=2
    for j in range(0,n):
        dp[0][j]=1
        dp[1][j]=2

    for i in range(2,m):
        for j in range(2,n):
            algo5_helper(i,j,tt,dp)
            if dp[i][j]>max_size:
                max_size=dp[i][j]
                res_x=i
                res_y=j

    return res_x-max_size+2,res_y-max_size+2,res_x+1,res_y+1

m,n,h=list(map(lambda x: int(x),input().split(" ")))
arr=[]
for i in range(m):
  arr.append(list(map(lambda x: int(x),input().split(" "))))

ans=task5a(arr,h)

for i in ans:
  print(i,end=" ")