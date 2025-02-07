import json 
def abrirJSON():
    dicFinal={}
    with open(".casoestudi.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./casoestudi.json",'w') as outFile:
        json.dump(dic,outFile)
bo=True
while bo==True