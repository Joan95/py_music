import numpy as np
import matplotlib.pyplot as pl

from notes import Note

samples_per_second = 44100
speed_of_sound = 343


'''
    p = sound pressure 
    w = angular frequency/velocity
    t = time
    T = period
    f = frequency 
    x = position
    k = wave number
    
    p = p0 sin(wt +- kx)
    w = 2pi/T; w = 2pi f
'''


class Wave:
    def __init__(self, _note, _amplitude=1):
        self.note = Note(_note)
        self.wave_length = None
        self.amplitude = _amplitude
        self.period = None
        self.velocity = speed_of_sound
        self.samples = None
        self.wave = None

    def generate_wave(self, seconds=1):
        self.samples = np.arange(seconds * samples_per_second) / samples_per_second
        self.wave = np.sin(2 * np.pi * self.note.freq * self.samples)
        self.print_wave()

    def print_wave(self):
        pl.plot(self.samples, self.wave)
        pl.xlabel("Time s (samples)")
        pl.ylabel("Wave Amplitude")
        pl.show()

