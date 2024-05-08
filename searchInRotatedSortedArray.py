## suppose an array sorted in ascending order and is rotated at a pivot and given a target value to search for
 
class Solution:
 	def search(self, nums:list[int], target:int) -> int:
 		l, r = 0, len(nums) -1

 		while l <= r: 
 			mid = (l + r) // 2
 			if target == mid: 
 				return mid

 			if nums[mid] >= nums[l]:
 				if target > nums[mid] or target < nums[l]:
 					l = mid +1
 				else:
 					r = mid -1

 			else: 
 				if target < nums[mid] or target > nums[r]:
 					r = mid -1
 				else:
 					l = mid +1

 		return -1
