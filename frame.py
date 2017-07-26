# coding=UTF-8

'''
Created on 11 nov. 2014

@author: pclf
'''

import pygame

class Frame(object):
	def __init__(self):
		self.point_list = []

	def LineTo(self, xy, c):
		'''
		USAGE   : - Frame.LineTo(tuple,int) 
		RESUME  : - Crée un tuple entre une liste de coordonées spatiale et un entier colorimétrique.
		ENTREE  : - xy : liste (x,y) d'un point.
				: - c  : entier hexadécimale codant la couleur.
		SORTIES : - VOID
		'''
		self.point_list.append((xy + (c,))) # Ecrire (c,) permet de le convertir en mono-tuple. 
	
	def Line(self, xy1, xy2, c):
		self.LineTo(xy1,0)
		self.LineTo(xy2,c)
	
	def PolyLineOneColor(self, xy_list, c, closed=False):
		'''
		USAGE   : - Frame.PolyLineOneColor(list of tuple, int, boolean)
		RESUME  : - Crée une liste de 2 tuples contenant la position x,y et la couleur de deux points formant une ligne,
				    le premier point à la couleur blanche, le dernier à la couleur donnée par c.
		ENTREES : - xy_list est la liste des coordonnées spatiales sous forme de tuples.
				  - c  : entier hexadécimale codant la couleur.
				  - closed : Définit la fin de la ligne si égal à True. False sinon.
		SORTIES : - VOID
		'''
		xy0 = None   # Si aucun point n'a été utilisé pour le moment.
		for xy in xy_list:  # Alors pour chaque points dans la liste.
			if xy0 is None: # Si aucun point n'a encore été analysé.
				xy0 = xy    # Alors enregistrer le premier point.
				self.LineTo(xy0,0) # Lui assigner la couleur blanche.
			else:                  # 
				self.LineTo(xy,c) 
		if closed:
			self.LineTo(xy0,c)
	
	def RenderScreen(self, surface):
		xyc_prev = self.point_list[0]
		#pygame.draw.line(surface,self.black_hole_color,(x_bh_cur, y_bh_cur), (x_bh_next, y_bh_next))
		#pygame.draw.line(surface,self.spoke_color,(x_bh_cur, y_bh_cur), (x_area_cur, y_area_cur))
		for xyc in self.point_list:
			c = int(xyc[2])
			if c: pygame.draw.line(surface,c,xyc_prev[:2],xyc[:2],3)
			xyc_prev = xyc

class FrameHolder(object):
	def __init__(self):
		self.f = None
		
