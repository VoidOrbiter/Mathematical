import numpy as np

def calculate_iqr(x_arr):
    data = sorted(x_arr)
    n = len(data)

    if n < 2:
        return 0.0
    
    def get_median(ls):
        m = len(ls)
        if m == 0: return 0
        if m % 2 == 0:
            return (ls[m//2 - 1] + ls[m//2]) / 2
        return ls[m//2]
    
    if n % 2 == 0:
        lower_half = data[:n//2]
        upper_half = data[n//2:]
    else:
        lower_half = data[:n//2 + 1]
        upper_half = data[n//2:]
    
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)

    return float(q3 - q1)


def calculate_skewness(x_arr):
    n = len(x_arr)
    if n < 3:
        return 0.0
    
    mean = np.mean(x_arr)
    std_dev = np.std(x_arr, ddof=1)

    if std_dev == 0:
        return 0.0
    
    z_scores = (x_arr - mean) / std_dev
    sum_cubed_z = np.sum(z_scores**3)

    correction = n / ((n - 1)*(n - 2))

    return correction * sum_cubed_z

def calculate_excess_kurtosis(x_arr):
    n = len(x_arr)
    if n < 4:
        return "N/A (n<4)"
    
    mean = sum(x_arr) / n
    variance = sum((x - mean)**2 for x in x_arr) / (n - 1)
    std_dev = variance**0.5

    if std_dev == 0:
        return 0.0
    
    fourth_moment = sum(((x - mean) / std_dev) ** 4 for x in x_arr)

    term1 = (n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))
    term2 = (3 * (n - 1)**2) / ((n - 2) * (n - 3))

    kurtosis = (term1 * fourth_moment) - term2
    return kurtosis

def calculate_standard_error(std_dev, x_arr):
    n = len(x_arr)
    if n <= 0:
        return 0.0
    std_err = std_dev / (n**0.5)
    return std_err