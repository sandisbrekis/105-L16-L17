# 170.py
# Sandis Brēķis
# 121REB474

from math import sin, fabs
from time import sleep

def f(x):
 return sin (x)
# Definejam argumenta x robezhas :
 a = 1.1
 b = 3.2

# Aprekjina funkcijas vertibas dotajos punktos :
 funa = f(a)
 funb = f(b)

# Parbauda vai dotajaa intervala ir saknes:
 if ( funa * funb > 0.0 ):
 print " Dotaja intervala [%s, %s] saknju nav "%(a,b)
 sleep (1); exit ()
 else:
 print " Dotaja intervala sakne (s) ir!"

# Definejam precizitati, ar kadu meklesim sakni :
 deltax = 0.01

# Sashaurinam saknes mekleshanas robezas :
 while ( fabs (b-a) > deltax ):
 x = (a+b)/2; funx = f(x)
 if ( funa*funx < 0. ):
 b = x
 else :
 a = x
 print "Sakne ir: ", x