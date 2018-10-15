#!/usr/bin/env python
# -*- coding: utf-8 -*-

# recoge de un fichero los tweets para irlos retwiteando cada vez que ejecutemos el script
# >> retuitewa.py -f fichero.txt
import sys

import tweepy
from secret import *


def retweet():
    api = init_twitter('sysmanapy')
    yo = api.me()

    input_file = open(ftuits,'r')
    file_lines=input_file.readlines()

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
    # print "Retweet de estado ",tuit," realizado con éxito"
