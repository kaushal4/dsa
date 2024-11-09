class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hand = sorted(hand)
        expectation = [0] * n
        current = 0
        i = 0
        group_num = 0

        while i < n:
            if group_num > 0 and hand[i] != hand[i-1] + 1:
                return False
            count = 1
            j = i + 1
            while j < n and hand[i] == hand[j]:
                count += 1
                j+= 1
            if group_num > count or (current + groupSize > n and count - group_num > 0):
                return False
            if count- group_num > 0:
                expectation[current + groupSize - 1] += count - group_num
            group_num = count
            group_num -= expectation[current]
            expectation[current] = 0
            current += 1
            i = j
        print(expectation)

        return sum(expectation) == 0