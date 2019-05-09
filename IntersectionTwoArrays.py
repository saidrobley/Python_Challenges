class IntersectionArrays:
    def intersect(self, nums1 : [int], nums2: [int]) ->[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        index = 0
        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                # del nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                # del nums2[j]
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
                index += 1

        return res
