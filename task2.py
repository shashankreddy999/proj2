def task2(arr,h):
  m=len(arr)
  n=len(arr[0])
  max_size=0
  res_x,res_y=0,0

  for i in range(m):
    for j in range(n):
      if arr[i][j]>=h:
        curr_size=1
        flag=True
        while i+curr_size<m and j+curr_size<n and flag:
          for k in range(j,j+curr_size+1):
            if arr[i+curr_size][k]<h:
              flag=False
              break
          for k in range(i,i+curr_size+1):
            if arr[k][j+curr_size] < h:
              flag=False
              break
          
          if flag:
            curr_size=curr_size+1
        if curr_size>max_size:
          max_size=curr_size
          res_x=i
          res_y=j
  return res_x+1,res_y+1,res_x+max_size,res_y+max_size

m,n,h=list(map(lambda x: int(x),input().split(" ")))
arr=[]
for i in range(m):
  arr.append(list(map(lambda x: int(x),input().split(" "))))

ans=task2(arr,h)

for i in ans:
  print(i,end=" ")