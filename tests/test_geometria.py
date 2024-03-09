import this
from math import sqrt
from unittest import TestCase

from geometria.geometria import area_triangulo, area_triangulo_equilatero


class test_area_triangulo(TestCase):

    def test_triangulo_com_entrada_valida(self):
        assert area_triangulo(10, 20) == 100
        assert area_triangulo(7, 7) == 24.5
        assert area_triangulo(sqrt(5), 8) == 8.94

    def test_triangulo_com_entrada_invalida(self):
        assert area_triangulo(0, 0) == "Valor de entrada invalido"
        assert area_triangulo(0, 10) == "Valor de entrada invalido"
        assert area_triangulo(20, 0) == "Valor de entrada invalido"
        assert area_triangulo(-10, 2) == "Valor de entrada invalido"
        assert area_triangulo(30, -2) == "Valor de entrada invalido"


class teste_triangulo_equilatero(TestCase):
    def test_area_triangulo_valido(self):
        assert area_triangulo_equilatero(12) == 62.35

    def test_triangulo_com_lado_invalido(self):
        self.lado = -10
        area_triangulo = area_triangulo_equilatero(self.lado)
        self.assertEqual(area_triangulo, "Digite um lado valido")
