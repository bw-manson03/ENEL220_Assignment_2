import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

signal_noisy = np.loadtxt('Desktop/ecg_noisy.txt', skiprows=1)
signal_og = np.loadtxt('Desktop/ecg_original.txt', skiprows=1)

cutoff_frequency = 50  #Cutoff frequency in Hz
sampling_rate = 1000   #Sampling rate in Hz

order = 1  # Filter order (1 for regular low-pass filter)
nyquist = 0.5 * sampling_rate
normalized_cutoff = cutoff_frequency / nyquist
b, a = butter(order, normalized_cutoff, btype='low', analog=False)

filtered_signal = filtfilt(b, a, signal_noisy)
np.savetxt('filtered_signal.txt', filtered_signal)


time = np.arange(len(signal_noisy)) / sampling_rate
plt.figure(figsize=(10, 6))
plt.plot(time, signal_noisy, label='Noisy Signal', linewidth=1)
plt.plot(time, signal_og, label='Original Signal', linewidth=1)
plt.plot(time, filtered_signal, label='Filtered Signal (50 Hz Low Pass)', linewidth=1)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Low-Pass Filtered Signal')
plt.show()