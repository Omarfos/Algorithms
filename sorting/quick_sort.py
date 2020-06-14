
class Solution:
    def quick_sort(self, nums, low, high):
        if low < high:
            q = self.partition(nums, low, high)
            self.quick_sort(nums, low, q-1)
            self.quick_sort(nums, q+1, high)
        return nums

    def partition(self, nums, low, high):
        key = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= key:
                i = i + 1
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

        nums[high] = nums[i+1]
        nums[i+1] = key
        return i + 1

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_one(self):
        r = self.solution.quick_sort([2,1], 0, 1)
        self.assertEqual(r,[1,2])
    def test_two(self):
        r = self.solution.quick_sort([5,7,6,3,4,0,2,1], 0, 7)
        self.assertEqual(r,[0,1,2,3,4,5,6,7])


if __name__ == '__main__':
    unittest.main()

           
