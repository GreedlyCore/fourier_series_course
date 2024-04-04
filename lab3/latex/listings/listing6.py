def plot_sound(wave, time, caption = '', ):
    # remove some time to aboid problem with indexing
    t = np.linspace(0, time - 2, 10000)
    plt.figure(figsize=(8, 5)) 

    plt.plot(t, wave(t))
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.legend(['sound'], loc='lower right')
    plt.title(caption)
    plt.grid()

plot_sound(sound_from_time, length, caption='Waveform of accord7.mp3',)
