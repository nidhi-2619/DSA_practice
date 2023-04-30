def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    prev1 = 0
    prev2 = 0
    for i in range(1,n):
        fs = prev1+abs(heights[i]-heights[i-1])
        ss = float('inf')
        if i>1:
            ss = prev2 + abs(heights[i]-heights[i-2])
            
        prev2 = prev1
        prev1 = min(fs,ss)
    return prev1    
