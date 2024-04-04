def f1(t):
    if abs(t) <= b:
        return a
    elif abs(t) > b:
        return 0

vec_f1 = np.vectorize(f1)