class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    major = int(len(nums) / 2)
    numsDict = {}
    
    for n in nums:
      count = numsDict.get(n)
      if (not count): 
        count = 0
      count += 1  
      if (count >= major):
        return n
      numsDict[n] = count

if __name__ == '__main__':
  sol = Solution()

  # Test 1
  # Input: nums = [3,2,3]
  # Output: 3

  testCase1 = {
    'nums': [3,2,3]
  }
  print(sol.majorityElement(testCase1['nums']))