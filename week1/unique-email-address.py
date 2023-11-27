class Solution:
  def numUniqueEmails(self, emails: list[str]) -> int:
    sanitized_emails = {}
    for email in emails:
      local, domain = email.split('@')
      local = "".join(local.split("."))
      local = local.split("+")[0]
      sanitize_email = local+'@'+domain

      if (sanitized_emails.get(sanitize_email)):
        continue
      else:
        sanitized_emails[sanitize_email] = 1
    return len(sanitized_emails.values())

if __name__ == '__main__':
  sol = Solution()

  #TestCase 1:
  
  # Input: emails = [
  #   "test.email+alex@leetcode.com",
  #   "test.e.mail+bob.cathy@leetcode.com",
  #   "testemail+david@lee.tcode.com"
  # ]
  # Output: 2

  testCase1 = {
    'emails': [
      "test.email+alex@leetcode.com",
      "test.e.mail+bob.cathy@leetcode.com",
      "testemail+david@lee.tcode.com"
    ]
  }

  print(sol.numUniqueEmails(testCase1['emails']))