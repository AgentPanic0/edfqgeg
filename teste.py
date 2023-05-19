import vlc
import time
import requests

###### CONFIGURACOES ######
#URL = "rtsp://admin:IAIICC13@146.164.69.149:554/cam/realmonitor?channel=1&subtype=0"
URL = "http://146.164.69.149/cgi-bin/mjpg/video.cgi?&subtype=1"
chunk_size =256
r = requests.get(URL, stream=True)

with open("123.mp4", "wb") as f:
	for chunk in r.iter_content(chunk_size=chunk_size):
		f.write(chunk)

####### FUNC AUX ##############
def Abrir_transmissao(url):
	
	media = vlc.MediaPlayer(url)

	media.play()

	time.sleep(5)

	parada = 0

	while media.is_playing() and parada == 0:
	    parada = input ()

	media.stop()

	print("A midia parou")

	return 0

###### Main #######
def main(nome_arquivo):

	descritor_arquivo = open(nome_arquivo, "w")

	Abrir_transmissao(URL)

	descritor_arquivo.close()

	return 0

#main("Gravacao.mp4")..
