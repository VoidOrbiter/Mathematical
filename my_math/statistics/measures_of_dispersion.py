import numpy as np

def sample_variance(x_arr):
    n = len(x_arr)
    if n < 2:
        return 0.0
    mu = np.mean(x_arr)
    sum_of_square = 0.0
    sum_of_absolute_diff = 0.0
    
    for x_i in x_arr:
        diff = x_i - mu
        sq_diff = diff ** 2
        sum_of_square += sq_diff
        sum_of_absolute_diff += abs(diff)

    variance = sum_of_square / (n - 1)
    std_dev = np.sqrt(variance)
    mean_absolute_deviation = sum_of_absolute_diff / n
    coefficient_of_variation = (std_dev / mu) * 100

    return variance, std_dev, mean_absolute_deviation, coefficient_of_variation