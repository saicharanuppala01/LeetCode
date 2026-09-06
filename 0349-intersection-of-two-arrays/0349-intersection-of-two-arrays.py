class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        ans = set()
        for i in nums1:
            seen.add(i)
        for j  in nums2:
            if j in seen:
                ans.add(j)
        return list(ans)