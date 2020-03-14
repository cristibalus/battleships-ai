
probabilitateInitiala = 1 / 84
probabilitatiInitialeCap = [[], [], [], [], [], [], [], [], [], []]

def probabilitatePatratel(rand, coloana):
  return 0 if eImposibilSaFieCap(rand, coloana) else probabilitateInitiala

def eImposibilSaFieCap(rand, coloana):
  return (rand in [0, 1, 8, 9]) and (coloana in [0, 1, 8, 9])

def matriceInitiala():
  probabilitati = probabilitatiInitialeCap

  for rand in list(range(10)):
    probabilitatiInitialeCap[rand] = []
    for coloana in list(range(10)):
      probabilitatiInitialeCap[rand].append(probabilitatePatratel(rand, coloana))

  return probabilitati
