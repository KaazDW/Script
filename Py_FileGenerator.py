# -*- coding: utf-8 -*-
# github.com/kaazdw
# script permettant de générer x fichier dans le répertoire dans lequel est présent le script python
x = 10000
for nombre in range(0,x):
    f = open("MonFichier%s.txt" % nombre,'w')
    nombre = nombre + 1
        