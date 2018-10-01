def quick_sort(alist,start,end):
    """快速排序"""
    if start >= end:
        return
    mid = alist[start]
    left = start
    right = end

    while left < right:
        while left < right and alist[right] >= mid:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]
    alist[left] = mid

    quick_sort(alist,start,left-1)
    quick_sort(alist,left+1,end)

if __name__ == "__main__":
    alist = [123,312,31,2,54,77,4] 
    quick_sort(alist,0,len(alist)-1)
    print(alist)

