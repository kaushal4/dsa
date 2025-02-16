class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        sol:List[List[str]] = []
        email_index:Dict[str, int] = {}

        for account in accounts:
            is_duplicate = False
            duplicate_index = []
            for email in account[1:]:
                if email in email_index:
                    is_duplicate = True
                    duplicate_index.append(email_index[email])
            if is_duplicate:
                duplicate_index = list(set(duplicate_index))
                base_index = duplicate_index[0]
                for email in account[1:]:
                    sol[base_index].append(email)
                    email_index[email] = base_index
                for other_index in duplicate_index[1:]:
                    for email in sol[other_index][1:]:
                        sol[base_index].append(email)
                        email_index[email] = base_index
                    sol[other_index] = []
            else:
                sol.append(account)
                new_index = len(sol) - 1
                for email in account[1:]:
                    email_index[email] = new_index
        
        sol = [x for x in sol if x != []]
        
        for i in range(len(sol)):
            email_set = set(sol[i][1:])
            emails = list(email_set)
            emails.sort()
            sol[i][1:] = emails
        
        
        return sol