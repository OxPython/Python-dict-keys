'''
Created on Jul 1, 2014

@author: viejoemer
'''
############################################################
#HowTo get the keys of a dict in python?

#Creating a dict with data

d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }

#get de keys of a dict
r = d.keys()


print(type(r))
print(r)


for i in r:
    print(i)
    
print(d)