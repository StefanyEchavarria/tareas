import decimal
 
a1 = decimal.Decimal(input('a1: '))
b1 = decimal.Decimal(input('b1: '))
c1 = decimal.Decimal(input('c1: '))
 
a2 = decimal.Decimal(input('a2: '))
b2 = decimal.Decimal(input('b2: '))
c2 = decimal.Decimal(input('c2: '))
def pinta_ecuacion(a, b, c):
    dev = ''
    if a != 0:
        dev += '%sx' % a
    if b > 0:
        dev += ' + %sy ' % b
    elif b < 0:
        dev += ' %sy ' % b
    dev += ' = %s' % c
 
    return dev
 
print(pinta_ecuacion(a1, b1, c1))
print(pinta_ecuacion(a2, b2, c2))
 
numerador_y = a2*c1 - a1*c2
denominador_y = a2*b1 - a1*b2
 
# método ce cálculo de la posición de rectas:
paralelas = a1*b2 == a2*b1
if paralelas:
    coincidentes = a1*c2 == a2*c1
    if coincidentes:
        print('Rectas coincidentes')
    else:
        print('Rectas paralelas')
else:
    # son secantes. calculo el punto de intersección
    if a1 == 0:
        y = c1/b1
        x = (c2-b2*y)/a2
    else:
        y = numerador_y/denominador_y
        x = (c1-b1*y)/a1
 

    print('Son secantes. Punto intersección: (%s, %s)' % (x, y))
