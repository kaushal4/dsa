class Solution:
    def findMax(self, freqs, intervals):
        max_key = '.'
        max_key_val = 0
        for key in freqs:
            if freqs[key] > max_key_val and intervals[key] == 0:
                max_key_val = freqs[key]
                max_key = key
        return max_key

    def leastInterval(self, tasks: List[str], n: int) -> int:
        t_len = len(tasks)
        freqs = dict()
        intervals = dict()
        sol = 0
        for t in tasks:
            if t in freqs:
                freqs[t] += 1
            else:
                freqs[t] = 1
                intervals[t] = 0

        while(t_len > 0):
            t_len-= 1

            # wait for some time if no task is ready
            cheapest = min(intervals.values())
            for key in intervals:
                intervals[key] = max(0, intervals[key] - cheapest - 1)
            sol += max(cheapest, 1)

            # select task to do
            task_to_do = self.findMax(freqs=freqs, intervals=intervals) 

            # run the task
            freqs[task_to_do] -= 1
            intervals[task_to_do] = n+1

            # remove the currtly run element if it is fully processed 
            if freqs[task_to_do] == 0:
                freqs.pop(task_to_do)
                intervals.pop(task_to_do)


        return sol