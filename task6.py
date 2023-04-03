def task6(arr, h, k):
    m = len(arr)
    n = len(arr[0])
    max_size = 0
    res_x, res_y = 0, 0
    b, r = 0,0

    for i in range(m):
        for j in range(n):
            width=min(m-i+1, n-j+1)
            for d in range(1, width):
                #print('aaa')
                t = 0
                for x in range(i, i+d):
                    for y in range(j, j+d):
                        if arr[x][y] < h:
                            #print('ok')
                            t += 1
                            
                if t <= k and d > max_size:
                    #print(t,k)
                    max_size = d
                    res_x, res_y = i, j
                    b, r = i+d-1, j+d-1

    return res_x+1, res_y+1, b+1, r+1
m,n,h,k=list(map(lambda x: int(x),input().split(" ")))
arr=[]
for i in range(m):
  arr.append(list(map(lambda x: int(x),input().split(" "))))

ans=task6(arr,h,k)

for i in ans:
  print(i,end=" ")