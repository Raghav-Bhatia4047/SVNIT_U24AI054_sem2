# 5. Write a program to make the length of each element 15 of a given Numpy array and the 
# string centred, left-justified, right-justified with paddings of _ (underscore). 
import numpy as np
lst = []
N = int(input("Enter the number of terms: "))
for _ in range(N):
    a = input()
    lst.append(a)
arr = np.array(lst)
centered = np.array([x.center(15,"_") for x in lst])
left = np.array([x.ljust(15,"_") for x in lst])
right = np.array([x.rjust(15,"_") for x in lst])
print(centered)
print(left)
print(right)