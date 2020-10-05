import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def Traducao(palavra):
    if palavra in data:
        return data[palavra]
    elif len(get_close_matches(palavra,data.keys())) > 0:
        verificando = input("Voce quis dizer %s? S- Sim. N- Nao. " % get_close_matches(palavra, data.keys())[0])
        verificando = verificando.upper()
        if (verificando == "S"):
            return data[get_close_matches(palavra, data.keys())[0]]
        elif (verificando == "N"):
            return "Palavra nao encontrada"
        else:
            return "Entrada nao entendida!"        
    else:
        return "Palavra nao encontrada"


Palav = input("Digite uma palavra: ")
Palav = Palav.lower()

saida = Traducao(Palav)

if type(saida) == list:
    for item in saida:
        print(item)
else:
    print(saida)