#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot=list(mot)
    for i in range(0,len(mot)):
        mot[i]= chr(ord(mot[i]) - 32)
    mot=''.join(mot)
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
