class Solution:
    def lastTarget(self,ar,e):
        ans = -1
        start,end=0,len(ar)-1
        while start<=end:
            mid = start+(end-start)//2
            if ar[mid]==e:
                ans = mid
                start = mid+1
            elif ar[mid]>e:end=mid-1
            else:start = mid+1
        return ans
    def firstTarget(self,ar,e):
        res = -1
        start = 0
        end = len(ar)-1
        while start<=end:
                mid = start+(end-start)//2
                if ar[mid]==e:
                    res = mid
                    end = mid-1
                elif ar[mid]<e:start=mid+1
                else:end = mid-1
        return res        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        RES =  [-1,-1]
        RES[0] = self.firstTarget(nums,target)
        RES[1] = self.lastTarget(nums,target)    
        return RES
