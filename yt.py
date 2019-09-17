from __future__ import unicode_literals
import youtube_dl

def obtenerUrl():
	archivo = open("lista.txt", "r")
	cadena = archivo.readlines()
	lista = cadena[0].split(",")
	lista.pop((len(lista)-1))
	archivo.close()
	return lista

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

for x in obtenerUrl():
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([x])
