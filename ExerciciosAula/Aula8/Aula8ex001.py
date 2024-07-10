from math import pow, sqrt, hypot
num1 = float(input('Comprimento do cateto oposto: '))
num2 = float(input('Comprimento do cateto adjacente: '))
'''hi = pow(num1,2) + pow(num2,2)
c = sqrt(hi)'''
hi = hypot(num1, num2)
print('A hipotenusa e {:.2f}'.format(hi))

'''
num1 = float(input('Comprimento do cateto oposto: '))
num2 = float(input('Comprimento do cateto adjacente: '))
hi = (pow(num1,2) + pow(num2,2)) ** (1/2) 
'''
