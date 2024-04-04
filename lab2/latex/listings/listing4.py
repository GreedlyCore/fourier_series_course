def f6(t):
  T = t+c
  if abs(T) <= b:
    return a - abs(a*T/b)
  elif abs(T) > b:
    return 0

vec_f6 = np.vectorize(f6)

def f6_image(omega):
  return f2_image(omega) * np.exp(1j*omega*c)