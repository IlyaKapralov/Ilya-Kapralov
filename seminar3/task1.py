import matplotlib.pyplot as plt
import numpy as np
import copy
from math import ceil 

class audio():
    def __init__(self,filename:str) -> None:
        file0bj = open("1kHz_44100Hz_16bit_05sec.wav", mode = "rb")
        data = file0bj.read()
        file_size_inbytes = data [4:8] 
        file_size = int.from_bytes(file_size_inbytes, byteorder = "little")

        print ('рамер файла - ',file_size)

        num_of_channels_in_byte = data[22:24]
        num_of_channels = int.from_bytes(num_of_channels_in_byte, byteorder = "little")

        print ('colvo canalov - ',num_of_channels)

        audio_data_size_in_bytes = data[40:44]
        audio_data_size =int.from_bytes(audio_data_size_in_bytes, byteorder = "little")

        print ('audio_data -',audio_data_size)

        audio_amps = []

        sample_rate_in_bytes = data [24:28]
        sample_rate = int.from_bytes(sample_rate_in_bytes, byteorder = "little")

        print ('chastota discr - ',sample_rate)

        for i in range (0,audio_data_size,2):
            amp_in_byte = data[44+i:44+i+2]
            amp = int.from_bytes(amp_in_byte, byteorder = "little", signed = True)
            audio_amps.append(amp)

# xdata = range(0,len(audio_amps)/sample_rate, 1/sample_rate)
xdata = np.linspace(0,len(audio_amps)/sample_rate, len(audio_amps))

#plt.plot(xdata,audio_amps)
#plt.show()

spectre = np.fft.fft(audio_amps)
abs_spectre = abs (spectre)
print (abs_spectre)

plt.plot(1/xdata,abs_spectre)
plt.show()

pass