def task7b(arr, h, k):
    m = len(arr)
    n = len(arr[0])
    temp = [[[-1, set()] for j in range(n)] for i in range(m)]
    max_size = 0
    res_x, res_y = 0, 0
    b, r = 0, 0

    for i in range(m):
        for j in range(n):
            if i != 0 and j != 0:
                pass
            else:
                if arr[i][j] < h and k >= 1:
                    temp[i][j][0] = 1
                    temp[i][j][1].add((i, j))
                elif arr[i][j] >= h:
                    temp[i][j][0] = 1
                else:
                    temp[i][0] = 0
                    temp[i][j][1].add((i, j))
                continue

            mt,ml,md = temp[i-1][j], temp[i][j-1], temp[i-1][j-1]

            size = min(mt[0], ml[0], md[0])
            
            if not helper(temp, mt, ml, md, arr, size, h, k, i, j):
                pass
            else:
                if max_size >= temp[i][j][0]:
                    pass
                else:
                    max_size = temp[i][j][0]
                    res_x, res_y = i+1-max_size, j+1-max_size

    return res_x+1,res_y+1,res_x+max_size,res_y+max_size


def helper(temp, mt, ml, md, arr, size, h, k, b, r):
    check = k
    if arr[b][r] >= h:
        pass
    else:
        
        check -= 1
        temp[b][r][1].add((b, r))

    res_x = b - size
    res_y = r - size

    for c in mt[1]:
        if check < 0:
            break
        if res_x <= c[0] <= b and res_y <= c[1] <= r:
            if c in temp[b][r][1]:
                pass
            else:
                check -= 1
                temp[b][r][1].add(c)

    for c in ml[1]:
        if check < 0:
            break
        if res_x <= c[0] <= b and res_y <= c[1] <= r:
            if c  in temp[b][r][1]:
                pass
            else:
                check -= 1
                temp[b][r][1].add(c)

    for c in md[1]:
        if check < 0:
            break
        if res_x <= c[0] <= b and res_y <= c[1] <= r:
            if c not in temp[b][r][1]:
                check -= 1
                temp[b][r][1].add(c)

    if check >= 0:
        temp[b][r][0] = size + 1
        return True
        
    else:
        temp[b][r][0] = 0
        return False

m,n,h,k=list(map(lambda x: int(x),input().split(" ")))
arr=[]
for i in range(m):
  arr.append(list(map(lambda x: int(x),input().split(" "))))

ans=task7b(arr,h,k)

for i in ans:
  print(i,end=" ")