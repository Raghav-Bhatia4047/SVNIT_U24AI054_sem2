# 4. Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space. 
# Store them in a numpy array.  Convert them to polar coordinates.


import numpy as np


def cartesian_to_polar(points):
    polar_points = []
    for x, y in points:
        r = np.sqrt(x*2 + y*2)  #
        theta = np.arctan2(y, x)  
        polar_points.append((r, theta))
    return np.array(polar_points)


N = int(input("Enter the number of points (N >= 10): "))
if N < 10:
    print("Please enter a value of N that is at least 10.")
else:
    cartesian_points = []
    print(f"Enter {N} points in the format 'x y':")
    for _ in range(N):
        x, y = map(float, input().split())
        cartesian_points.append((x, y))

   
    cartesian_array = np.array(cartesian_points)

   
    polar_array = cartesian_to_polar(cartesian_array)

    print("\nPolar coordinates (r, θ):")
    print(polar_array)