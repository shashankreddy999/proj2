def task7a(arr, h,kk):
    m = len(arr)
    n = len(arr[0])
    res_x, res_y = 0, 0
    b, r = 0,0
    
    dp = [[0] * (n + 1) for i in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            
            if arr[i-1][j-1] >= h:
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
    
    
    max_size = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            k = 0
            while i + k < m+1 and j + k < n+1:
                v = dp[i+k][j+k] - dp[i+k][j-1] - dp[i-1][j+k] + dp[i-1][j-1]
                no = pow((k+1),2) - v
                
                if no > kk:
                    pass
                else:
                    if max_size >= pow((k+1),2):
                        pass
                    else:
                        res_x,res_y = i, j 
                        b,r = i+k, j+k
                        max_size = pow((k+1),2)
                k += 1
    return res_x,res_y,b,r

m,n,h,k=list(map(lambda x: int(x),input().split(" ")))
arr=[]
for i in range(m):
  arr.append(list(map(lambda x: int(x),input().split(" "))))

ans=task7a(arr,h,k)

for i in ans:
  print(i,end=" ")