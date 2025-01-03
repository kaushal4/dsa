class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def find(num:int):
            if num % 2 == 0:
                return 2
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return i
            return num
        
        smallest = nums[n-1]
        op = 0
        for i in range(n-1,-1,-1):
            new_num = nums[i]
            while new_num > smallest:
                temp = find(new_num)
                op += 1
                if new_num == temp:
                    return -1
                new_num = temp

            if new_num < smallest:
                smallest = new_num

        return op