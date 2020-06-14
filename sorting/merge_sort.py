import sys

class Solution:
    def merge_sort(self, nums, low, high):
        print(f"sorting: {low} :: {high}")
        if low < high:
            mid = low + (high - low) // 2
            self.merge_sort(nums, low, mid)
            self.merge_sort(nums, mid+1, high)
            self.merge(nums, low, mid, high)
        return nums

    def merge(self, nums, low, mid, high):
        print(f"Merging: {low},{mid} :: {mid+1},{high}")
        a = nums[low:mid+1]  
        b = nums[mid+1:high+1]
        a.append(sys.maxsize) #sentinel values to simplify checking
        b.append(sys.maxsize)
        i = j = 0
        for k in range(low, high+1):
            if a[i] <= b[j]:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = b[j]
                j += 1

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_one(self):
        r = self.solution.merge_sort([2,1], 0, 1)
        self.assertEqual(r,[1,2])
    def test_two(self):
        r = self.solution.merge_sort([5,7,6,3,4,0,2,1], 0, 7)
        self.assertEqual(r,[0,1,2,3,4,5,6,7])


if __name__ == '__main__':
    unittest.main()

           
