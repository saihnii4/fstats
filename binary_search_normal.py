import scipy.stats as stats
import numpy as np
import sys

INF = 10


def eq(p, v, t):
    return (p + t) > v and v > (p - t)


def binary_search(target, l=-INF, r=INF, tolerance=0.0000000001):
    test = (l + r) / 2
    prob = stats.norm.cdf([test])[0]
    if eq(target, prob, tolerance):
        return (test, abs(prob - target))

    if prob > target:
        return binary_search(target, l, test)
    else:
        return binary_search(target, test, r)


probability = sys.argv[1]
z_value, discrepancy = binary_search(np.float64(probability))

print(z_value)
print(discrepancy)
