from imports import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        distinct_emails = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0].replace(".", "")
            distinct_emails.add(local_name + "@" + domain_name)

        return len(distinct_emails)
