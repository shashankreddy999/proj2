def task1(arr,h):
  m=len(arr)
  n=len(arr[0])
  max_size=0
  res_x,res_y=0,0

  for x in range(m):
    for y in range(n):
      width=min(m-x,n-y)
      for d in range(width):
        if all(arr[x+a][y+b]>=h for a in range(d+1) for b in range(d+1)):
          if d+1>max_size:
            max_size=d+1
            res_x=x
            res_y=y
            
  return res_x+1,res_y+1,res_x+max_size,res_y+max_size

m,n,h=list(map(lambda x: int(x),input().split(" ")))
arr=[]
for i in range(m):
  arr.append(list(map(lambda x: int(x),input().split(" "))))

ans=task1(arr,h)

for i in ans:
  print(i,end=" ")