import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, TransferFunction, lsim

# RLC Band-Pass Filter Design Parameters
R = 31.4            # Resistance in ohms
L = 10e-3           # Inductance in henries
C = 2.81e-7         # Capacitance in farads
f_center = 3000     # Center frequency in Hz (3rd harmonic)
f_input = 1000      # Frequency of input square wave (1 kHz)
f_sample = 100e3    # Sampling frequency for simulation
duration = 0.01     # Duration of the signal in seconds

t = np.arange(0, duration, 1/f_sample)
input_signal = square(2 * np.pi * f_input * t)

# Transfer function for RLC circuit: H(s) = sL / (s^2*LC + sRC + 1)
num = [L, 0]
den = [L*C, R*C, 1]
system = TransferFunction(num, den)
t_out, output_signal, _ = lsim(system, input_signal, t)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, input_signal, label='Input Signal (1 kHz Square Wave)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Input Signal (1 kHz Square Wave)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t_out, output_signal, color='orange', label='Filtered Output (3 kHz Band-Pass)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Filtered Output Signal (Isolated 3 kHz Component)')
plt.grid(True)

plt.tight_layout()
plt.show()
