class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1), len(nums2)
        if n>m:
            nums1,nums2 = nums2,nums1
            n,m = len(nums1), len(nums2)
        half = (n+m)//2
        l, r = 0, n
        while l<=r:
            m1 = (l+r)>>1
            m2 = half - m1
            # print(l,r,m1,m2)
            l1 = nums1[m1-1] if m1>0 else -float('inf')
            r1 = nums1[m1] if m1<n else float('inf')
            l2 = nums2[m2-1] if m2>0 else -float('inf')
            r2 = nums2[m2] if m2<m else float('inf')
            if (l1>r2):
                r = m1-1
            elif (l2>r1):
                l = m1+1
            else:
                if (n+m)&1:
                    return min(r1,r2)
                return (min(r1,r2) + max(l1,l2))/2
        

            