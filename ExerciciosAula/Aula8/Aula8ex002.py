import math
angulo = float(input('Digite o ângulo que você deseja: '))
vcos = math.cos(math.radians(angulo))
vtan = math.tan(math.radians(angulo))
vsen = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, vsen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, vcos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, vtan))
