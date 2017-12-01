'''
Created on 2017. 9. 17.

@author: jihye
'''
import math 
value = 15
sqrtValue=math.sqrt(value)
print('sqrt of %d : %-10.5f' %(value,sqrtValue))

print ('e : %10.8f' %math.e)
print('pi : %10.8f' %math.pi)

d = math.pi/3
sinValue=math.sin(d)
cosValue=math.cos(d)
print('sin(pi/3) : %-10.8f' %sinValue)
print('cos(pi/3) : %-10.8f' %cosValue)

a = 2**3.5
b = pow(2, 3.5)
c = math.pow(2, 3.5)

print ( 'using ** operator -2^3 : %-10.8f' %a )
print ( 'using built-in pow function -2^3 : %-10.8f ' %b)
print ( 'using math pow function -2.3 : %-10.8f ' %c)
