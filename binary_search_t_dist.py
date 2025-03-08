import scipy.stats as stats
import numpy as np
import sys

INF = 10


def eq(p, v, t):
    return (p + t) > v and v > (p - t)


def binary_search(target, df, l=-INF, r=INF, tolerance=0.0000000001):
    test = (l + r) / 2
    prob = stats.t.cdf([test], df)[0]
    if eq(target, prob, tolerance):
        return (test, abs(prob - target))

    if prob > target:
        return binary_search(target, df, l, test)
    else:
        return binary_search(target, df, test, r)


probability = sys.argv[1]
df = sys.argv[2]
z_value, discrepancy = binary_search(np.float64(probability), int(df))

print(z_value)
print(discrepancy)
