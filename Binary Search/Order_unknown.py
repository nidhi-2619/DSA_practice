# first try to find if array is in ascending order or descending order
a = [1,2,3,4,5,6,7]
e = 2
if len(a)==1:return a[0]
else:
  start,end = 0,len(a)-1
  if a[0]>a[1]:
      while start<=end:
        mid = start+(end-start)//2
        if a[mid]==e:
          return mid
        elif a[mid]<e:
          end = mid-1
        else:start=mid+1
  else:  
    while start<=end:
        mid = start+(end-start)//2
        if a[mid]==e:
          return mid
        elif a[mid]<e:
          start = mid+1
        else:end=mid-1
