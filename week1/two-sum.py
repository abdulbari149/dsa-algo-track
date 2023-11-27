class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    nums_dict = {}
    
    n = len(nums)

    for i in range(n):
      first = nums[i]
      second = target - nums[i]
      if (second in nums_dict):
        return [i, nums_dict[second]]
      else:
        nums_dict[first] = i


if __name__ == '__main__':
  sol = Solution()

  # Test 1
  # nums = [2,7,11,15], target = 9
  # Output: [0,1]
  testCase1 = {
    'nums': [2,7,11,15],
    'target': 9
  }
  print(sol.twoSum(**testCase1))