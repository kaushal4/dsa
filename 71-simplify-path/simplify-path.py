class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        sol = []
        for directory in directories:
            if len(directory) == 0: continue
            if directory == '.': continue
            if directory == '..':
                if sol:
                    sol.pop()
            else:
                sol.append(directory)
        ans = ''
        for dir in sol:
            ans += '/' + dir
        if not ans:
            return '/'
        return ans