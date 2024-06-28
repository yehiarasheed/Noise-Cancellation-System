import numpy as np 
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
##from scipy.signal import find_peaks, peak_widths

t = np. linspace(0 , 3 , 12 * 1024)

x1 = (np.sin(2 * np.pi * 0 *t) + np.sin(2 * np.pi * 261.63 * t)) * (np.heaviside(t-0,1) - np.heaviside(t-0.6,1))
x2 = (np.sin(2 * np.pi * 0 *t) + np.sin(2 * np.pi * 493.88 * t)) * (np.heaviside(t-0.7,1) - np.heaviside(t-0.9,1))
x3 = (np.sin(2 * np.pi * 0 *t) + np.sin(2 * np.pi * 349.23 * t)) * (np.heaviside(t-1,1) - np.heaviside(t-1.5,1))
x4 = (np.sin(2 * np.pi * 0 *t) + np.sin(2 * np.pi * 493.88 * t)) * (np.heaviside(t-1.6,1) - np.heaviside(t-1.8,1))
x5 = (np.sin(2 * np.pi * 0 *t) + np.sin(2 * np.pi * 440 * t)) * (np.heaviside(t-1.9,1) - np.heaviside(t-2.1,1))
x6 = (np.sin(2 * np.pi * 0 *t) + np.sin(2 * np.pi * 329.63 * t)) * (np.heaviside(t-2.2,1) - np.heaviside(t-2.4,1))
x7 = (np.sin(2 * np.pi * 0 *t) + np.sin(2 * np.pi * 293.66 * t)) * (np.heaviside(t-2.5,1) - np.heaviside(t-2.7,1))
x8 = (np.sin(2 * np.pi * 0 *t) + np.sin(2 * np.pi * 261.63 * t)) * (np.heaviside(t-2.8,1) - np.heaviside(t-3.0,1))

x = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8

#plot sound in time domain
plt.figure()
plt.plot(t, x)

#play sound 

sd.play(x, 3 * 1024)

N = 3*1024
f = np.linspace(0,512,int(N/2))
x_f=fft(x)
x_f=(2/N)*np.abs(x_f[0:int(N/2)])

#plot sound in freq domain
plt.figure()
plt.plot(f,x_f)

fn1 = np.random.randint(0,512,1)
fn2 = np.random.randint(0,512,1)
n_t=np.sin(2*fn1*np.pi*t)+np.sin(2*fn2*np.pi*t)
x_nt=x+n_t
x_f = fft(x_nt)
x_fn = 2/N * np.abs(x_f[0:int(N/2)])

#plot noise in time domain
plt.figure()
plt.plot(t,x_nt)

#sd.play(x_nt, 3 * 1024)

#plot time in freq domain
plt.figure()
plt.plot(f,x_fn)
temp=x_fn
peak1 = np.max(x_fn)
xpeak1tuple = np.where(x_fn == peak1)
xpeak1index = xpeak1tuple[0]
xpeak1indexz=xpeak1index[0]
freq1 = round(f[xpeak1indexz])
temp[xpeak1indexz]=0

peak2 = np.max(temp)
xpeak2tuple = np.where(x_fn == peak2)
xpeak2index = xpeak2tuple[0]
xpeak2indexz=xpeak2index[0]
freq2 = round(f[xpeak2indexz])
print(freq2)

x_filtered = x_nt - (np.sin(2*freq1*np.pi*t)+np.sin(2*freq2*np.pi*t))
xfinal=fft(x_filtered)
xfinal= 2/N * np.abs(xfinal[0:int(N/2)])

#plot cancellation in freq domain
plt.figure()
plt.plot(f,xfinal)

#plot cancellation in time domain
plt.figure()
plt.plot(t,x_filtered)

#play after noise cancellation


sd.play(x_filtered, 4 * 1024)

