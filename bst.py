import numpy as np

print("Print the index where No. 3 is located at:", np.searchsorted([1,2,3,4,5], 3))

print("Print the index of the 'Gamma'" ,np.searchsorted(['Alpha', 'Beta', 'Delta', 'Gamma'], 'Gamma'))


if __name__=='__main__':
	print('bst.py is being run directly')