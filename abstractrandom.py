# -*- coding: utf-8 -*-

from globalVars import *  # Variables d'ajustement spatial du laser.
import random

SPEED = 4

class Absrand(object):
    def __init__(self):
        self.x, self.y = screen_size[0]/2, screen_size[1]/2 # Attributs x,y initialement centrés.
        self.last_xy = (self.x, self.y)
        self.speed = SPEED
        self.color = 0xFF00

    def Move(self,up_key,down_key,left_key,right_key):
		'''
		RESUME  : Génère des mouvements aléatoire suivant les 4 directions, les 
		4 clés sont des boolées et valent 0 si la direction est interdite, 1 
		sinon.
		ENTREES : Les 4 clés directionnelles.
		SORTIE  : RIEN
		'''
        self.last_xy = (self.x, self.y)
        random.seed()   # Génère des nombres aléatoires mais sauvegardés.
        direction = random.randint(0,4)
        self.speed += random.randint(0,40)-20

        if up_key or direction == 0:
            self.y -= self.speed
        elif down_key or direction == 1:
            self.y += self.speed
        if left_key or direction == 2:
            self.x -= self.speed
        elif right_key or direction == 3:
            self.x += self.speed
        # Reject bad points
        if self.x < 0:
            self.x = 0
        elif self.x >= screen_size[0]:
            self.x = screen_size[0]
        if self.y < 0:
            self.y = 0
        elif self.y >= screen_size[1]:
            self.y = screen_size[1]

    def Launch(self, f):
        random.seed()  # Génère une série de valeurs aléatoire sauvegardées.
        x_dir = self.x + 10*random.randint(-20,20)  # Crée une nouvelle position aléatoirement suivant x.
        y_dir = self.y + 10*random.randint(-20,20)  # Crée une nouvelle position aléatoirement suivant x.
        self.color = colorshex[random.randint(0,len(colorshex)-1)]  # Sélectionne une couleur aléatoire.
        f.PolyLineOneColor([(self.x, self.y), (x_dir, y_dir)], self.color, False) # Voir frame.py

    def Draw(self, f):
        random.seed()
        self.size = 10*random.randint(0,20)
        xmin = self.x - self.size
        xmax = self.x + self.size
        ymin = self.y - self.size
        ymax = self.y + self.size

        self.colorchange = random.randint(0,10)
        if self.colorchange == 0:
            self.color = colorshex[random.randint(0,len(colorshex)-1)]
	f.PolyLineOneColor([(xmin,ymin),(xmin,ymax),(xmax,ymax),(xmax,ymin)], self.color,True)


