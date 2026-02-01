from my_math.statistics.central_tendency import central_tendency

def central_tendency_calculate(x_arr):
   
    arithmetic_mean, harmonic_mean, geometric_mean, median = central_tendency(x_arr)

    results = {
        "arithmetic": arithmetic_mean,
        "harmonic": harmonic_mean,
        "geometric": geometric_mean,
        "median": median
    }

    return results