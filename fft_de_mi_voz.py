import scikits.audiolab as audio
import pyplot as plt
from scipy.fftpack import fft, fftfreq
#%pylab inline

input_signal, sampling_rate, enc = audio.wavread("minombre.wav")


fft_mivoz = fft(input_signal)/len(input_signal)
frecuencia = fftfreq(len(input_signal), 1)
plt.plot(frecuencia, fft_mivoz)

save("mivoz_fft", ext="png", close=False, verbose=True)
