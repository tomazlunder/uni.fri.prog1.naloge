__author__ = 'Tommy'
from math import *

v = float(input("Vnesi hitrost izstrelka (m/s):"))
kot = float(input("Vnesi kot izstrelka (v stopinjah):"))
s = ((v)**2 * sin(radians(2*kot))) / float(9.8)

print("Izstrelek bo letel", s ,"metrov.")
