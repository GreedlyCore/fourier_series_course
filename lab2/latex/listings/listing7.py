def dot_prod(f, g, a, b):
    x = np.linspace(a, b, 1000)
    dx = x[1] - x[0]
    return np.dot(f(x), g(x)) * dx

def wave_fourier_image(func, a, b):
    image = lambda v: dot_prod(func, lambda t: np.e ** (-2 * np.pi * 1j * v * t), a, b)
    return np.vectorize(image)

# TRANSFORM
wave_image = wave_fourier_image(sound_from_time, 0, 0.09)
wave_image_abs = lambda t: abs(wave_image(t))
plot_wave_image(wave_image_abs, 0, 4000, caption='Accord7 freqs image')
