## design a class to find th Kth largest element in a stream 

class KthLargest:

	def __init__(self, k:int, nums:list[int]):

		self.minHeap, self.k = nums, k
		heapq.heapify(self.minHeap)
		while len(self.minHeap) > k:
			heapq.heappop(self.minHeap)


	def add(self, val:int) -> int:
		heapq.heappush(self.minHeap, val)
		if len(minHeap) > self.k: 
			heapq.heappop(self.minHeap)
		return self.minHeap[0]