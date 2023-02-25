# binary search implementation

def binary_search(start,end,arr,element):
  start,end=0,len(arr)-1
  while start<=end:
#     we do this to avoid interger overflow
    mid = start+(end-start)//2
    if arr[mid]==element:
      return mid
    elif arr[mid]<element:
      start = mid+1
    else:
      end = mid-1
  return -1 #if element is not found    
        
index = binary_search(arr,e)    
    
