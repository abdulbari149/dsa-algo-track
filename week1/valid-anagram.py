class Solution:
  def count_letters(self, s:str):
    count_s = {}
    for a in s:
        if count_s.get(a):
            count_s[a] += 1
        else:
            count_s[a] = 1
    return count_s

  def isAnagram(self, s: str, t: str) -> bool:    
    if len(s) != len(s):
        return False

    letter_count_of_s = self.count_letters(s)
    letter_count_of_t = self.count_letters(t)

    for letter in s:
        if not letter_count_of_t.get(letter):
            return False
        if letter_count_of_s[letter] != letter_count_of_t[letter]:
            return False
    return True

if __name__ == '__main__':
  sol = Solution()

  #TestCase 1:
  # Input: s = "anagram", t = "nagaram"
  # Output: true
  testCase1 = {
    's': 'anagram',
    't': 'nagaram'
  }

  print(sol.isAnagram(testCase1['s'], testCase1['t']))

