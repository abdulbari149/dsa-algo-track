class Solution:
  def containsDuplicate(self, nums: list[int]) -> bool:
    count = {}
    for n in nums:
      if count.get(n):
          return True
      else:
          count[n] = 1
    return False

if __name__ == '__main__':
  sol = Solution()

  #TestCase 1:
  # Input: nums = [1,2,3,1]
  # Output: true
  testCase1 = {
    'nums': [1,2,3,1]
  }
  print(sol.containsDuplicate(testCase1['nums']))
