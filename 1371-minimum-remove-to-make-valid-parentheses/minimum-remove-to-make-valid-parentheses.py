class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # set of indices to remove
        to_remove = set()
        # remove if unmatched )
        # remove all remaining (

        # list of indices of ( which are unmatched
        unmatch = []

        q = list(s)

        for index, c in enumerate(q):
            if c == ')':
                if len(unmatch) == 0:
                    to_remove.add(index)
                else:
                    unmatch.pop()
            elif c == '(':
                unmatch.append(index)
        to_remove.update(unmatch)

        sol = ""

        for index, c in enumerate(q):
            if index in to_remove:
                continue
            sol = sol + c
        
        return sol


