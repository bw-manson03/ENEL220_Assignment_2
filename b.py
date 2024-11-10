import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

cutoff_frequency = 50  # Cutoff frequency in Hz
sampling_rate = 1000   # Sampling rate in Hz
R = 1e3                # Resistance in ohms
C = 3.18e-6            # Capacitance in Farads

numerator = [1]
denominator = [R * C, 1]
system = signal.TransferFunction(numerator, denominator)
frequencies = np.logspace(0, 4, 1000)  # From 1 Hz to 10,000 Hz
w, mag, phase = signal.bode(system, frequencies * 2 * np.pi)  # Convert to rad/s

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.semilogx(w / (2 * np.pi), mag)  # Convert rad/s back to Hz for x-axis
plt.title('Bode Plot of RC Low-Pass Filter')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid(which="both", linestyle="--")

plt.subplot(2, 1, 2)
plt.semilogx(w / (2 * np.pi), phase)  # Convert rad/s back to Hz for x-axis
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [degrees]')
plt.grid(which="both", linestyle="--")

plt.tight_layout()
plt.show()
