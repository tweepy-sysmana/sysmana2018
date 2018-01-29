#!/usr/bin/env python
# -*- coding: utf-8 -*-

# recoge de un fichero los tweets para irlos retwiteando cada vez que ejecutemos el script
# >> retuitewa.py -f fichero.txt
import sys
if 'idlelib.rpc' in sys.modules:
    sys.argv.extend(raw_input("Args: ").split())
import tweepy
from secret import *

# Se comprueba que reciba por parámetro un fichero donde leer los tweets
if len(sys.argv)<2:
    print   "Usage:",sys.argv[0],"-f file\n\n",
    sys.exit(1)

# Recogemos el fichero
if '-f' in sys.argv:    #fichero
    ftuits=sys.argv[sys.argv.index('-f')+1]
else:
    print "No hay fichero de tuits"
    sys.exit(1)

api = init_twitter('sysmanapy')
yo = api.me()

input_file=open(ftuits,'r')
file_lines=input_file.readlines()
# Extraemos el primer tweet de la lista
n=0                             
while n<len(file_lines):
    l=file_lines[n].split('/')
    # comprobamos que se corresponda con un tweet
    if l[0][:4]=="http" and l[2]=="twitter.com" and l[4]=="status":
        tuit=l[5].strip('\n')
        break   
    n+=1

file_lines=file_lines[n+1:]     # Sobreescribimos el fichero extrayendo el tweet
input_file.close()
output_file=open(ftuits,'w')
output_file.writelines(file_lines)
output_file.close()

#Y se retwitea
api.retweet(tuit)
print "Retweet de estado ",tuit," realizado con éxito"
