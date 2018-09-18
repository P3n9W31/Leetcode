class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [-1]*len(nums1)
        for num_index in range(len(nums2)):
            if nums2[num_index] in nums1:
                index = nums1.index(nums2[num_index])
                now = num_index
                while now != len(nums2) - 1:
                    now += 1
                    if nums2[now] > nums2[num_index]:
                        bigger = nums2[now]
                        ans[index] = bigger
                        break
        return ans
        