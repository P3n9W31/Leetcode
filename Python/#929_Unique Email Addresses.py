class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_email = set()
        for email in emails:
            at_place = email.index('@')
            email_localname = email[:at_place]
            email_domin = email[at_place:]
            email_localname = email_localname.replace('.','')
            if '+' in email_localname:
                email_localname = email_localname[:email_localname.index('+')]
                
            new_email = email_localname + email_domin
            unique_email.add(new_email)
            
        return len(unique_email)
        