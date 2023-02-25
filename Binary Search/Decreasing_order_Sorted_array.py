# the code will be same as the binary search but only with few modification
a  = [9,8,7,6,5,4,3,2,1]
e = 6
start,end=0,len(a)-1
while start<=end:
  if a[start]==e:
    print(mid)
    exit()
  elif a[start]>e:
    start = mid-1
  else:  end = mid+1
print(-1)    
    
