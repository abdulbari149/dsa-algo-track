class Solution:
  def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
    ans = []
    for n in nums1:            
      i = len(nums2) - 1
      first_greatest = -1
      while (i >= 0 and n != nums2[i]):
          if (nums2[i] > n):
              first_greatest = nums2[i]  
          i -= 1
      ans.append(first_greatest)
    return ans

if __name__ == '__main__':
  sol = Solution()

  #TestCase 1:
  # Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
  # Output: [-1,3,-1]

  testCase1 = {
    'nums1': [4,1,2],
    'nums2': [1,3,4,2]
  }
  print(sol.nextGreaterElement(testCase1['nums1'], testCase1['nums2']))