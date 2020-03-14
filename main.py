from probabilitati_initiale_cap import matriceInitiala
from numpy import array, where
from random import choice
from shoot import shootTest
from shoot import shoot
from login import login

cazuriPosibile = 85
probabilitati = matriceInitiala()
mascaStanga = [[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 1, 0]]
mascaDreapta = [[0, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1], [0, 1, 0, 0]]
mascaSus = [[0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0]]
mascaJos = [[0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0]]

def updateProbabilitatiNimic(probabilitati, x, y, cazuriPosibile, lovite):
    for i in range(10):
        for j in range(10):
            if probabilitati[i][j] > 0 and lovite[i][j] == -1:
                probabilitati[i][j] = 1/cazuriPosibile

def calculeazaCazuriCorp(x, y, mask):
    posibilitatiCorp = 0
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 1 and probabilitati[x + i][y + j] > 0:
                posibilitatiCorp += 1
    return posibilitatiCorp

def aplicaProbabilitatiCorp(x, y, mask, probabilitate, lovite):
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 1 and probabilitati[x + i][y + j] > 0 and lovite[x+i][y+j] == -1:
                probabilitati[x + i][y + j] -= probabilitate
            if mask[i][j] == 1 and probabilitati[x + i][y + j] <= 0 and lovite[x+i][y+j] == -1:
                probabilitati[x + i][y + j] += probabilitate

def updateProbabilitatiCap(probabilitati, x, y, cazuriPosibile, lovite):
    posibilitatiCorp = 0

    if x-3>=0 and y-2>=0 and y+2<=9:
        posibilitatiCorp += calculeazaCazuriCorp(x-3, y-2, mascaSus)
    elif x+3<=9 and y-2>=0 and y+2<=9:
        posibilitatiCorp += calculeazaCazuriCorp(x, y-2, mascaJos)
    elif x-2>=0 and x+2<=9 and y-3>=0:
        posibilitatiCorp += calculeazaCazuriCorp(x-2, y-3, mascaStanga)
    elif x-2>=0 and x+2<=9 and y+3<=9:
        posibilitatiCorp += calculeazaCazuriCorp(x-2, y, mascaDreapta)

    probabilitateCorp = posibilitatiCorp/cazuriPosibile
    probabilitateRest = (cazuriPosibile - posibilitatiCorp)/cazuriPosibile

    for i in range(10):
        for j in range(10):
            if probabilitati[i][j] > 0 and lovite[i][j] == -1:
                probabilitati[i][j] += probabilitateRest
            

    if x-3>=0 and y-2>=0 and y+2<=9:
        aplicaProbabilitatiCorp(x-3, y-2, mascaSus, probabilitateCorp, lovite)
    elif x+3<=9 and y-2>=0 and y+2<=9:
        aplicaProbabilitatiCorp(x, y-2, mascaJos, probabilitateCorp, lovite)
    elif x-2>=0 and x+2<=9 and y-3>=0:
        aplicaProbabilitatiCorp(x-2, y-3, mascaStanga, probabilitateCorp, lovite)
    elif x-2>=0 and x+2<=9 and y+3<=9:
        aplicaProbabilitatiCorp(x-2, y, mascaDreapta, probabilitateCorp, lovite)

capuriLovite = 0
performanta = 0
token = login()
def updateProbabilitatiCorp(probabilitati, x, y, cazuriPosibile, lovite):
    posibilitatiCap = 0

    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x-4, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x-3, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x-2, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x-1, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x-2, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x-3, y)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x-2, y)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaDreapta, x-1, y)

    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x-4, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x-3, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x-2, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x-1, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x-2, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x-3, y-3)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x-2, y-3)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaStanga, x-1, y-3)

    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-1, y)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-1, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-1, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-1, y-3)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-1, y-4)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-2, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-3, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-3, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaSus, x-3, y-3)

    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x-2, y)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x-2, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x-2, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x-2, y-3)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x-2, y-4)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x-1, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x, y-1)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x, y-2)
    posibilitatiCap += calculeazaProbabilitateCap(probabilitati, mascaJos, x, y-3)

    posibilitateCap = 0
    if posibilitatiCap != 0:
      posibilitateCap = 1/posibilitatiCap


    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x-4, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x-3, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x-2, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x-1, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x-2, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x-3, y, posibilitateCap, lovite)
    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x-2, y, posibilitateCap, lovite)
    calculeazaProbabilitateCapDreapta(probabilitati, mascaDreapta, x-1, y, posibilitateCap, lovite)

    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x-4, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x-3, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x-2, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x-1, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x-2, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x-3, y-3, posibilitateCap, lovite)
    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x-2, y-3, posibilitateCap, lovite)
    calculeazaProbabilitateCapStanga(probabilitati, mascaStanga, x-1, y-3, posibilitateCap, lovite)

    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-1, y, posibilitateCap, lovite)
    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-1, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-1, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-1, y-3, posibilitateCap, lovite)
    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-1, y-4, posibilitateCap, lovite)
    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-2, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-3, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-3, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapSus(probabilitati, mascaSus, x-3, y-3, posibilitateCap, lovite)

    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x-2, y, posibilitateCap, lovite)
    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x-2, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x-2, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x-2, y-3, posibilitateCap, lovite)
    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x-2, y-4, posibilitateCap, lovite)
    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x-1, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x, y-1, posibilitateCap, lovite)
    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x, y-2, posibilitateCap, lovite)
    calculeazaProbabilitateCapJos(probabilitati, mascaJos, x, y-3, posibilitateCap, lovite)
    
def calculeazaProbabilitateCapStanga(probabilitati, mask, x, y, posibilitateCap, lovite):
    try:
      if x>0 and y>0 and lovite[x-2][y] == -1:
        probabilitati[x-2][y] += posibilitateCap
    except:
      pass

def calculeazaProbabilitateCapSus(probabilitati, mask, x, y, posibilitateCap, lovite):
    try:
      if x>0 and y>0 and lovite[x][y+2] == -1:
        probabilitati[x][y+2] += posibilitateCap
    except:
      pass

def calculeazaProbabilitateCapJos(probabilitati, mask, x, y, posibilitateCap, lovite):
    try:
      if x>0 and y>0 and lovite[x+3][y+2] == -1:
        probabilitati[x+3][y+2] += posibilitateCap
    except:
      pass

def calculeazaProbabilitateCapDreapta(probabilitati, mask, x, y, posibilitateCap, lovite):
    try:
      if x>0 and y>0 and lovite[x+2][y+3] == -1:
        probabilitati[x+2][y+3] += posibilitateCap
    except:
      pass

def calculeazaProbabilitateCap(probabilitati, mask, x, y):
    try:
        for i in range(len(mask)):
            for j in range(len(mask[i])):
                if mask[i][j] == 1 and lovite[x + i][y + j] == 0:
                    return 0
        return 1
    except:
        return 0

  
lupta = "119"
print(lupta)

lovite = [[0, 0, -1, -1, -1, -1, -1, -1, 0, 0], [0, 0, -1, -1, -1, -1, -1, -1, 0, 0], [-1] * 10, [-1] * 10, [-1] * 10, [-1] * 10, [-1] * 10, [-1] * 10, [0, 0, -1, -1, -1, -1, -1, -1, 0, 0], [0, 0, -1, -1, -1, -1, -1, -1, 0, 0]]
while capuriLovite < 3:
    cazuriPosibile -= 1
    maxProbabilitate = max(map(max, probabilitati))
    
    (x, y) = tuple(choice(array(where(array(probabilitati) == maxProbabilitate)).T))   

    performanta += 1
    raspuns = int(shoot(str(y + 1), chr(65 + x), lupta, token))
    lovite[x][y] = raspuns
    # print("trage in: ", str(y), " ", chr(65 + x))
    # print("raspuns: ", raspuns)
    if raspuns == 0:
        updateProbabilitatiNimic(probabilitati, x, y, cazuriPosibile, lovite)
        probabilitati[x][y] = 0
    elif raspuns == 1:
        updateProbabilitatiCorp(probabilitati, x, y, cazuriPosibile, lovite)
        probabilitati[x][y] = -1
    elif raspuns == 2:
        print("trage in: ", str(y), " ", chr(65 + x))
        print("raspuns: ", raspuns)
        capuriLovite += 1
        updateProbabilitatiCap(probabilitati, x, y, cazuriPosibile, lovite)
        probabilitati[x][y] = -2
 
print(performanta)