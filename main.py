import requests
import time
from playsound import playsound


def tick(bpm, bpb=4):
    sleep = 60.0 / bpm
    counter = 3
    while True:
        counter += 1
        if counter % bpb:
            playsound('./MetroBar1.wav')
        else:
            playsound('./MetroBeat1.wav')
            counter = 0
        print counter+1
        time.sleep(sleep)

# url da api provedora das informacoes
url = 'https://songbpm.com/api/search'

query = raw_input("Digite musica/artista para buscar...\n")

data = {
    'query': query
}

r = requests.post(url, data)
if r.status_code == 201:
    res = r.json()
    songs = res['search']['songs']
    i = 0

    if len(songs) > 0:

        print("MUSICAS")

        for song in songs:
            song['id'] = i
            print(song['id']+1)
            print(song['artist'])
            print(song['title'])
            print(song['tempo'])
            i += 1
            print '\n'

        id_selected = raw_input("Selecione numero da musica para iniciar bpm...\n")
        try:
            val = int(id_selected) - 1

            song_metro = songs[val]
            tick(song_metro["tempo"], 4)

        except ValueError:
            print('ID nao encontrado')
else:
    print("Nenhuma musica encontrada")
