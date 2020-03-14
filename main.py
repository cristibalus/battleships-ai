from probabilitati_initiale_cap import matriceInitiala
from numpy import array, where
from random import choice
from shoot import shootTest
from login import login

cazuriPosibile = 84
probabilitati = matriceInitiala()
mascaStanga = [[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 1, 0]]
mascaDreapta = [[0, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1], [0, 1, 0, 0]]
mascaSus = [[0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0]]
mascaJos = [[0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0]]

def updateProbabilitatiNimic(probabilitati, x, y, cazuriPosibile):
    probabilitati[x][y] = 0
    for i in range(10):
        for j in range(10):
            if probabilitati[i][j] != 0:
                probabilitati[i][j] = 1/cazuriPosibile

def calculeazaCazuriCorp(x, y, mask):
    posibilitatiCorp = 0
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 1 and probabilitati[x + i][y + j] != 0:
                posibilitatiCorp += 1
    return posibilitatiCorp

def aplicaProbabilitatiCorp(x, y, mask, probabilitate):
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 1 and probabilitati[x + i][y + j] != 0:
                probabilitati[x + i][y + j] = probabilitate

def updateProbabilitatiCap(probabilitati, x, y, cazuriPosibile):
    probabilitati[x][y] = 0
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
            if probabilitati[i][j] != 0:
                probabilitati[i][j] = probabilitateRest

    if x-3>=0 and y-2>=0 and y+2<=9:
        aplicaProbabilitatiCorp(x-3, y-2, mascaSus, probabilitateCorp)
    elif x+3<=9 and y-2>=0 and y+2<=9:
        aplicaProbabilitatiCorp(x, y-2, mascaJos, probabilitateCorp)
    elif x-2>=0 and x+2<=9 and y-3>=0:
        aplicaProbabilitatiCorp(x-2, y-3, mascaStanga, probabilitateCorp)
    elif x-2>=0 and x+2<=9 and y+3<=9:
        aplicaProbabilitatiCorp(x-2, y, mascaDreapta, probabilitateCorp)

capuriLovite = 0
performanta = 0
token = login()

while capuriLovite < 3:
    cazuriPosibile -= 1
    maxProbabilitate = max(map(max, probabilitati))
    (x, y) = tuple(choice(array(where(array(probabilitati) == maxProbabilitate)).T))
    performanta += 1
    print("trage in: ", str(y), " ", chr(65 + x))
    raspuns = int(shootTest(str(y), chr(65 + x), token))
    print("raspuns: ", raspuns)
    if raspuns == 0:
        updateProbabilitatiNimic(probabilitati, x, y, cazuriPosibile)
    elif raspuns == 1:
        probabilitati[x][y] = 0
    elif raspuns == 2:
        capuriLovite += 1
        updateProbabilitatiCap(probabilitati, x, y, cazuriPosibile)

print(performanta)