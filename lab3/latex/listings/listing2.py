def plot_original_and_image(x, f, f_image):
  figure, axis = plt.subplots(1, 2, figsize=(10, 6))

  axis[0].plot(x, [f(t) for t in x])
  axis[0].set_title(f"Original func with (a, b) = ({a}, {b})")
  axis[0].set_xlabel('t')
  axis[0].set_ylabel('y(t)')

  axis[1].plot(x, [f_image(t) for t in x])
  axis[1].set_title(f"Fourier image with (a, b) = ({a}, {b})")
  axis[1].set_xlabel('t')
  axis[1].set_ylabel('y(t)')

  plt.show()