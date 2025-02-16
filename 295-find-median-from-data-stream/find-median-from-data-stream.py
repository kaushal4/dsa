class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        # add into the min heap
        if len(self.min_heap) == len(self.max_heap):
            if len(self.max_heap) == 0 or num > (-self.max_heap[0]):
                heapq.heappush(self.min_heap, num)
            else:
                big_num = - heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, big_num)
                heapq.heappush(self.max_heap, - num)
        # add into the max heap
        else:
            if num < self.min_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                small_num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -small_num)
                heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            big_num = - self.max_heap[0]
            small_num = self.min_heap[0]
            return (big_num + small_num)/2
        return self.min_heap[0]