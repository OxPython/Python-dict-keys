'''
Created on Jul 2, 2014

@author: viejoemer

HowTo get all the keys of a dict in python?

¿Cómo obtener todas las llaves de un diccionario en Python?

'''

#Creating a dict with data
d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }
print(d)

#get de keys of a dict
r = d.keys()
print(type(r))
print(r)

for i in r:
    print(i)