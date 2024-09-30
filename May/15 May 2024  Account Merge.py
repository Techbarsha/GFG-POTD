class Solution:
    def accountsMerge(self, accounts):
        # Code here
        # Create a dictionary to map emails to their respective names
        email_to_name = {}
        # Create a dictionary to map each email to a unique ID
        email_to_id = {}
        # Create a dictionary to store the union find parent for each email ID
        parent = {}
        
        # Assign unique IDs to each email and populate email_to_name
        id_count = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = id_count
                    parent[id_count] = id_count
                    id_count += 1
        
        # Define a find function for the union find structure
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Union emails belonging to the same person
        for acc in accounts:
            first_id = email_to_id[acc[1]]
            for email in acc[2:]:
                email_id = email_to_id[email]
                parent[find(email_id)] = find(first_id)
        
        # Group emails by their parent IDs
        merged_emails = {}
        for email in email_to_id:
            email_id = email_to_id[email]
            root_id = find(email_id)
            if root_id not in merged_emails:
                merged_emails[root_id] = [email]
            else:
                merged_emails[root_id].append(email)
        
        # Prepare the result in the required format
        result = []
        for root_id, emails in merged_emails.items():
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))
        
        return result
