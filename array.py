# Python program to demonstrate
# Structured array
import numpy as np


a = np.array([('Sana', 2, 21.0), ('Mansi', 7, 29.0)],
	dtype=[('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float64)])
			
# Sorting according to the name
b = np.sort(a, order='name')
print('Sorting according to the name', b)

# Sorting according to the age
b = np.sort(a, order='age')
print('\nSorting according to the age', b)
