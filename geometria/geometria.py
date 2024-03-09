import math

#Triangulo
def area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        return "Valor de entrada invalido"

    area = (base * altura) / 2
    return float(('%.2f' % area).rstrip('0').rstrip('.'))


def area_triangulo_equilatero(lado):
    if lado <= 0:
        return "Digite um lado valido"

    area = (math.sqrt(3) / 4) * lado * lado
    return float(('%.2f' % area).rstrip('0').rstrip('.'))


def perimetro(lista_lado):
    soma_lados = 0
    for i in lista_lado:
        if (lista_lado <= 0):
            return "Lista contem um lado menor ou igual a 0"
        soma_lados += lista_lado[i];

    return soma_lados


def heron(ladoA, ladoB, ladoC):
    if not condicao_existencia_triangulo(ladoA, ladoB, ladoC):
        return "Digite um triangulo valido"

    s = (ladoA + ladoB + ladoC) / 2
    return str(math.sqrt(s * (s - ladoA) * (s - ladoB) * (s - ladoC)))


def condicao_existencia_triangulo(ladoA, ladoB, ladoC):
    if ladoA <= 0 or ladoB <= 0 or ladoC <= 0:
        return False
    elif (ladoA + ladoB) < ladoC:
        return False
    elif (ladoA + ladoC) < ladoB:
        return False
    elif (ladoB + ladoC) < ladoA:
        return False
    return True

#Retangulo
def area_retangulo(base, altura):
    if base <= 0 or altura <= 0:
        return "Digite um valor de entrada valido"
    return base * altura


