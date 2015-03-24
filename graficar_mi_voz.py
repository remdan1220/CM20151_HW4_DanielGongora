import scikits.audiolab as audio
import pyplot as plt
#%pylab inline

input_signal, sampling_rate, enc = audio.wavread("minombre.wav")
print (input_signal[0:10]), sampling_rate, enc

time_array = arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate))

plt.plot(time_array[0:4000], input_signal[0:4000])
plt.xlabel("time(s)", fontsize=20)
plt.ylabel("Amplitude", fontsize=20)

save("mi_voz", ext="png", close=False, verbose=True)
