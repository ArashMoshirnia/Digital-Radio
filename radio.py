import scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from playsound import playsound
from scipy import signal

print("Reading Signal. Please wait...")
path = "input/input.txt"
data = np.loadtxt(path)
print("Reading Finished")
amplification_factor = 4
cnt = 0
while True:
    w0 = int(input("Please select a frequency (96k,144k,288k,240k) : \n"))
    print("Processing...")
    N = 480000  #sampling rate
    cosine_values = 0.5 * (np.exp(np.array([1j*i*w0*2*np.pi/N for i in range(len(data))])) +
                           np.exp(np.array([-1j*i*w0*2*np.pi/N for i in range(len(data))])))
    f = np.multiply(data,cosine_values)
    f = np.fft.fft(f)
    f *= amplification_factor

    for i in range(20000,len(f)-20000):
        f[i] = 0

    f = np.fft.ifft(f)
    file_name = 'mt' + str(cnt)+ '.wav'
    wav.write(file_name, N, f.astype(np.dtype('i2')))
    print("Done. Playing...")
    playsound(file_name)
    cnt += 1
    f = None


