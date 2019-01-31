class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        s = set()
        for email in emails:
            key, domain = email.split('@')

            i = key.find('+')
            if i != -1:
                key = key[:i]
            key = key.replace('.', '')

            s.add(key + '@' + domain)
        return len(s)
