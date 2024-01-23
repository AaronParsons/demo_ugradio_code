import ugradio
import numpy as np
import sys

sdr = ugradio.sdr.SDR()
data = sdr.capture_data()

filename = sys.argv[-1]
print(f'Writing to {filename}')
np.savez(filename, data=data)
