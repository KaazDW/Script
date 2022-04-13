# -*- coding: utf-8 -*-
# github.com/kaazdw
# script permettant de générer N mot de passe de L charactère aléatoire

import string
import random


print("")
print("")
print(",---.     . . .    |    ,---.                         |              ")
print("|---',---.| | |,---|    |  _.,---.,---.,---.,---.,---.|--- ,---.,---.")
print("|    `---.| | ||   |    |   ||---'|   ||---'|    ,---||    |   ||    ")
print("`    `---'`-'-'`---'    `---'`---'`   '`---'`    `---^`---'`---'`")
print("by KaazDW")
print("")
      
N=input("-- Combien de Mot de Passe souhaitez-vous générer ?")
L=input("-- Combien de caractère par Mot de Passe ?")
int_N = int(N)
int_L = int(L)
try:
    int(int_N)
    est_intN = True
except ValueError:
    est_intN = False
try:
    int(int_L)
    est_intL = True
except ValueError:
    est_intL = False


print("[Value N int]", est_intL)
print("[Value L int]", est_intN)

if est_intN == True & est_intL == True:
    for N in range(int_N):
        print("")
        print("> ", ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(int_L)))
else:
    print("Votre entré n'est pas une valeur numérique")
  
    

  