def check_parseval(f, f_image):
  INT1, err1 = spi.quad(lambda t: abs(f(t))**2, -10**7, 10**7)
  INT2, err2 = spi.quad(lambda omega: abs(f_image(omega))**2, -10**7, 10**7)
  print(f"integrals: {INT1}  {INT2}")
  print(f"errors: {err1}  {err2}")
  print(f"delta: {abs(INT1-INT2):.5f}")

check_parseval(vec_f1, f1_image)