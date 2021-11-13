class BinarySearchTree:
	"""
	Binary Search Tree
	"""
	def is_sorted(arr):
		"""
		Check if an array is sorted.
		:param arr: array
		:return: boolean
		"""
		return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

	@staticmethod
	def binary_search(arr, target):
		"""
		Implement binary search on a sorted array.
		:param arr: sorted array
		:param target: target value
		:return: index of target value
		"""
		if BinarySearchTree.is_sorted(arr):
			left = 0
			right = len(arr) - 1
			while left <= right:
				mid = (left + right) // 2
				if arr[mid] == target:
					return mid
				elif arr[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
		return -1