class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n
        mod = 10**9+7

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev = -1
            if stack:
                dp[i] = dp[stack[-1]]
                prev = stack[-1]
            dp[i] += (i - prev) * arr[i]
            stack.append(i)

        total_sum = 0
        for num in dp:
            total_sum = total_sum + num
            total_sum = total_sum % mod
            print(total_sum)

        return total_sum
        