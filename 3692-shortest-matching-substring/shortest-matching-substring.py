class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        def kmp(s, p)-> List[Tuple[int, int]]:
            m = len(s)
            n = len(p)
            #  aabaab => [0,1,0,1,2,3]
            def getPrefix(p) -> List[int]:
                low = 0
                high = 1
                sol = [0] * n
                while high < n:
                    if p[high] == p[low]:
                        sol[high] = low + 1
                        low += 1
                        high += 1
                    else:
                        if low == 0:
                            sol[high] = 0
                            high += 1
                        else:
                            low = sol[low-1]
                return sol
            prefix = getPrefix(p)
            s_p = 0
            p_p = 0
            ans = []
            while(s_p < m):
                if p_p == n:
                    ans.append((s_p - n, s_p - 1))
                    p_p = prefix[p_p - 1]
                if p[p_p] == s[s_p]:
                    p_p += 1
                    s_p += 1
                else:
                    if p_p == 0:
                        s_p += 1
                    else:
                        p_p = prefix[p_p-1]
            
            if p_p == n:
                ans.append((s_p - n, s_p - 1))
                p_p = prefix[p_p - 1]
            return ans

        [start, mid, end] = p.split("*")
        if start and mid and end:
            start_matches = kmp(s, start)
            mid_matches = kmp(s, mid)
            end_matches = kmp(s, end)
            #print(start_matches, mid_matches, end_matches)

            start_p = 0
            mid_p = 0
            end_p = 0
            sol = float('inf')

            while(start_p < len(start_matches) and mid_p < len(mid_matches) and end_p < len(end_matches)):
                if mid_matches[mid_p][0] <= start_matches[start_p][1]:
                    mid_p += 1
                elif end_matches[end_p][0] <= mid_matches[mid_p][1]:
                    end_p += 1
                else:
                    sol = min(sol, end_matches[end_p][1] - start_matches[start_p][0] + 1)
                    start_p += 1

            return int(sol) if sol!=float('inf') else -1
        elif (start and mid) or (start and end) or (mid and end):
            start = start
            mid = mid
            if not start:
                start = mid 
                mid = end
            if not mid:
                mid = end
            
            start_matches = kmp(s, start)
            mid_matches = kmp(s, mid)

            #print(start_matches, mid_matches)

            sol = float('inf')

            start_p = 0
            mid_p = 0
            sol = float('inf')

            while(start_p < len(start_matches) and mid_p < len(mid_matches)):
                if mid_matches[mid_p][0] <= start_matches[start_p][1]:
                    mid_p += 1
                else:
                    sol = min(sol, mid_matches[mid_p][1] - start_matches[start_p][0] + 1)
                    start_p += 1


            return int(sol) if sol!=float('inf') else -1
        elif (start or mid or end):
            start = start
            if mid:
                start = mid
            if end:
                start = end
            
            start_matches = kmp(s, start)

            #print(start_matches)
            if not start_matches:
                return -1
            return min([a[1] - a[0] + 1 for a in start_matches])

        return 0