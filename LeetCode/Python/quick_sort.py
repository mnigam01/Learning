nums = [10, 7, 8, 9, 1, 5]
def partition(l,r):
    val = nums[r]
    i = l-1
    for j in range(l,r):
        if nums[j]<val:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
    i+=1
    nums[i], nums[r] = nums[r], nums[i]
    return i

def quickSort(l,r):
    if l>=r:
        return 
    pi = partition(l,r)
    quickSort(l,pi-1)
    quickSort(pi+1,r)
    