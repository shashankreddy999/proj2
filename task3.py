def task3(arr,h):
  m = len(arr)
  n = len(arr[0])
  dp = [[0] * n for _ in range(m)]
  max_size = 0
  res_x,res_y=0,0
  
  for i in range(0,m):
    dp[i][0]= 0 if arr[i][0]<h else 1
  
  for j in range(0,n):
    dp[0][j]= 0 if arr[0][j]<h else 1

    
  for i in range(0,m):
    for j in range(0,n):
      if arr[i][j] >= h:
        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        if dp[i][j]>max_size:
          max_size=dp[i][j]
          res_x=i
          res_y=j
  return res_x-max_size+2,res_y-max_size+2,res_x+1,res_y+1

m,n,h=list(map(lambda x: int(x),input().split(" ")))
arr=[]
for i in range(m):
  arr.append(list(map(lambda x: int(x),input().split(" "))))

ans=task3(arr,h)

for i in ans:
  print(i,end=" ")