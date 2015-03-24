all: grabar_mi_nombre.x mi_voz.png mivoz_fft.png minombre.wav 

grabar_mi_nombre.x: grabar_mi_nombre.c
	cc grabar_mi_nombre.c -o grabar_mi_nombre.x

minombre.wav: grabar_mi_nombre.x
	./grabar_mi_nombre.x

mi_voz.png: graficar_mi_voz.py
	python graficar_mi_voz.py

mivoz_fft.png: fft_de_mi_voz.py
	python fft_de_mi_voz.py
