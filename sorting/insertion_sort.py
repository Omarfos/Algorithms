

class Solution:
    def insertion_sort(self, nums):
        for i, key in enumerate(nums):
            j = i - 1 
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j = j - 1
            nums[j+1] = key
        return nums




import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_one(self):
        r = self.solution.insertion_sort([2,1])
        self.assertEqual(r,[1,2])
    def test_two(self):
        r = self.solution.insertion_sort([3,4,0,2,1])
        self.assertEqual(r,[0,1,2,3,4])


if __name__ == '__main__':
    unittest.main()

           
