def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        for i in range(0,n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
if __name__ == "__main__":
    li = [1,11,2,34,8,54,7]
    print(li)
    bubble_sort(li)
    print(li)
