meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "XD": "Respuesta a algo que da mucha risa"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!):")
if word in meme_dict.keys():
    print("Lo que significa tu palabra es:", meme_dict[word])
else:
    print("Lo sentimos no tenemos esa palabra")
