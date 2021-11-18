import unittest
from unittest import TestCase
from bst import BinarySearchTree as BST
import numpy as np


class TestBinarySearch(TestCase):
	"""
	Test class for BinarySearchTree
	"""

	def test_binary_search(self):
		"""
		Test binary search implementation against numpy implementation.
		"""
		self.assertEqual(BST.binary_search([1, 2, 3, 4, 5], 3), np.searchsorted([1, 2, 3, 4, 5], 3))
		self.assertEqual(
			BST.binary_search(['Alpha', 'Beta', 'Delta', 'Gamma'], 'Gamma'),
			np.searchsorted(['Alpha', 'Beta', 'Delta', 'Gamma'], 'Gamma'))
		print('Binary search test passed.')


if __name__ == '__main__':
	unittest.main()