import scipy.stats

X = [5.7, 4.4, 4.9, 4.6, 5.2, 4.5]
Y = [4.8, 3.9, 4.1, 4.2, 4.7, 4.3, 5.3]


def get_W():
    ranks = {v: i + 1 for i, v in enumerate(sorted(X + Y))}

    m_sample, n_sample = (X, Y) if len(X) < len(Y) else (Y, X)
    m = len(m_sample)
    n = len(n_sample)
    R_m = sum([ranks[val] for val in m_sample])
    W = min(R_m, m * (m + n + 1) - R_m)

    print(W)
