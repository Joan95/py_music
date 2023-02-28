import numpy as np
import matplotlib.pyplot as pl
import simpleaudio as sa

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
    def __init__(self, note, amplitude=1):
        self.note = Note(note)
        self.wave_length = None
        self.amplitude = amplitude
        self.period = None
        self.velocity = speed_of_sound
        self.samples = None
        self.sin_wave = None
        self.modulated_wave = None

    def generate_wave(self, amplitude=1):
        self.generate_sin_wave(amplitude)
        self.modify_wave()
        self.play_wave()

    def generate_sin_wave(self, amplitude):
        self.amplitude = amplitude
        self.samples = np.arange(self.note.figure["time"] * samples_per_second)
        self.sin_wave = np.sin((2 * np.pi) * self.note.freq * self.samples / samples_per_second)
        self.sin_wave *= amplitude
        self.sin_wave = np.int16(self.sin_wave * 32767)

        # self.print_wave(self.sin_wave)

    def modify_wave(self):
        # "Fade in and fade out effect"
        self.modify_amplitude()

    def play_wave(self):
        play_ob = sa.play_buffer(np.int16(self.modulated_wave), 1, 2, samples_per_second)
        play_ob.wait_done()

    def modify_amplitude(self):
        modulator_hz = 0.50

        # Modulate the self.sin_wave (Sin wave)
        modulator = np.sin(2 * np.pi * modulator_hz * self.samples / samples_per_second)
        self.modulated_wave = modulator * self.sin_wave

        # self.print_wave(self.modulated_wave)
        pass

    def print_wave(self, wave):
        pl.plot(self.samples, wave)
        pl.xlabel("Time s (samples)")
        pl.ylabel("Wave Amplitude")
        pl.show()

