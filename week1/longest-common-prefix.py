class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    prefix = strs[0]
    prefix_size = len(prefix)
    for i in range(1, len(strs)):
      word = strs[i]
      word_size = len(word)

      if (prefix_size > word_size):
        prefix = prefix[0:word_size]
        prefix_size = len(prefix)
      elif (prefix_size < word_size):
        word = word[0:prefix_size]
        word_size = len(word)
      common_letters = ''
      for i in range(prefix_size): 
        if prefix[i] != word[i]:
          break
        else:
          common_letters += prefix[i]
      prefix = common_letters
      prefix_size = len(prefix)
      if (prefix == ''):
        break
    return prefix

if __name__ == '__main__':
  sol = Solution()

  #TestCase 1:
  # Input: strs = ["flower","flow","flight"]
  # Output: "fl"  

  testCase1 = {
    'strs': ["flower","flow","flight"]
  }
  print(sol.longestCommonPrefix(testCase1['strs']))