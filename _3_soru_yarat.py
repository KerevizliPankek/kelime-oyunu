#Oyun için gerekli her birinden 2 adet olmak üzere, sırasıyla 4, 5, 6, 7, 8, 9 ve 10 harfli kelimeleri çekelim ve hazır hale getirelim.
from imports import * 


def soru_yarat():
    ref=db.reference("/tdk")
    data=ref.get()
    liste = []
    counter = 0
    for i in range(14):
        kan = {"madde":""}
        while len(kan["madde"])!=int(4+counter):
            kan = data[random.randint(0,len(data)-1)]
        liste.append(kan)
        counter += 0.5
    return liste

print(soru_yarat())