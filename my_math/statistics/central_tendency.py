import numpy as np

def central_tendency(x_arr):
    x_arr = x_arr

    arithmetic_mean = sum(x_arr) / len(x_arr)

    if all(x > 0 for x in x_arr):
        product = 1.0
        for x in x_arr:
            product *= x
        geometric_mean = product ** (1.0 / len(x_arr))
    else:
        geometric_mean = "Error: >0 only"
    
    if all(x != 0 for x in x_arr):
        sum_reciprocals = 0.0
        for x in x_arr:
            sum_reciprocals += (1.0 / x)
        harmonic_mean = len(x_arr) / sum_reciprocals
    else:
        harmonic_mean = "Error: Non-Zeros only"
    
    median = np.median(x_arr)

    return arithmetic_mean, harmonic_mean, geometric_mean, median