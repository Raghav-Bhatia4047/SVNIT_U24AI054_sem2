# 6. The bisection method is a technique for finding solutions (roots) to equations with a single 
# unknown variable. Given a polynomial function f, try to find an initial interval off by 
# random probe.  Store all the updates in an Numpy array. Plot the root finding process using the matplotlib/pyplot library.


import numpy as np
import matplotlib.pyplot as plt
import random

def polynomial_function(x):
    
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(f, a, b, tol=1e-6):
   
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid interval: f(a) and f(b) must have opposite signs.")
    
    updates = []  
    while abs(b - a) > tol:
        c = (a + b) / 2
        updates.append(c)   
        if f(c) == 0 or abs(b - a) < tol:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    return np.array(updates), c


random.seed(42)
a = random.uniform(-10, 10)
b = random.uniform(-10, 10)
while polynomial_function(a) * polynomial_function(b) >= 0: 
    a = random.uniform(-10, 10)
    b = random.uniform(-10, 10)

updates, root = bisection_method(polynomial_function, a, b)

print(f"Root found: {root}")
print(f"Midpoint Updates: {updates}")


x = np.linspace(min(updates) - 1, max(updates) + 1, 500)
y = polynomial_function(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Polynomial Function")
plt.axhline(0, color="gray", linestyle="--", label="y=0")
plt.scatter(updates, [polynomial_function(u) for u in updates], color="red", label="Midpoints")
plt.title("Bisection Method: Root-Finding Process")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()