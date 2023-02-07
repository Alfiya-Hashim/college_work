dot 

import numpy as np
list1=[10,20,30,40,50]
list2=[1,2,3,4,5]
vector1=np.array(list1)
vector2=np.array(list2)
print("we created from a list1:")
print(vector1)
print("we created from a list2:")
print(vector2)
vector_product=vector1.dot(vector2)
print("dot product of two vector:",vector_product)
