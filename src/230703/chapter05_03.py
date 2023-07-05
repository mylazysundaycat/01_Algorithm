def quick_sort(A, left, right):
    if left<right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)

def partition(A, left, right):
    pivot = A[(left+right)//2]
    while left<=right:
        while A[left]<pivot:
            left += 1
        while A[right]>pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left, right = left+1, right-1
    return left
