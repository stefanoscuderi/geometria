from unittest import TestCase

from geometria.triangulo import area, perimetro, condicao_existencia_triangulo, heron, area_triangulo_equilatero


class test_area_triangulo(TestCase):

    def setUp(self) -> None:
        self.base = 10
        self.altura = 20

    def test_triangulo_com_entrada_valida(self):
        area_triangulo = area(self.base, self.altura)
        self.assertEqual(area_triangulo, 100)

    def test_triangulo_com_base_0(self):
        self.base = 0
        self.altura = 6
        area_triangulo = area(self.base, self.altura)
        self.assertEqual(area_triangulo, "Valor de entrada invalido")

    def test_triangulo_com_valor_negativo(self):
        self.base = 4
        self.altura = -2
        area_triangulo = area(self.base, self.altura)
        self.assertEqual(area_triangulo, "Valor de entrada invalido")


class test_perimetro_triangulo(TestCase):

    def setUp(self) -> None:
        self.ladoA = 30
        self.ladoB = 40
        self.ladoC = 50

    def test_triangulo_com_triangulo_invalido(self):
        self.ladoA = 100
        perimetro_triangulo = perimetro(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(perimetro_triangulo, "Digite um triangulo valido")

    def test_triangulo_com_triangulo_equilatero(self):
        self.ladoB = 30
        self.ladoC = 30
        perimetro_triangulo = perimetro(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(perimetro_triangulo, "90")


class test_existencia_triangulo(TestCase):
    def setUp(self) -> None:
        self.ladoA = 30
        self.ladoB = 40
        self.ladoC = 50

    def test_triangulo_valido(self):
        triangulo_valido = condicao_existencia_triangulo(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(triangulo_valido, True)

    def test_triangulo_invalido_ladoC(self):
        self.ladoC = 100
        triangulo_invalido = condicao_existencia_triangulo(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(triangulo_invalido, False)

    def test_triangulo_invalido_ladoB(self):
        self.ladoB = 100
        triangulo_invalido = condicao_existencia_triangulo(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(triangulo_invalido, False)

    def test_triangulo_invalido_ladoA(self):
        self.ladoA = 100
        triangulo_invalido = condicao_existencia_triangulo(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(triangulo_invalido, False)

    def test_triangulo_invalido_negativo(self):
        self.ladoA = -10
        triangulo_invalido = condicao_existencia_triangulo(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(triangulo_invalido, False)


class test_area_heron(TestCase):
    def setUp(self) -> None:
        self.ladoA = 30
        self.ladoB = 40
        self.ladoC = 50

    def test_triangulo_com_triangulo_invalido(self):
        self.ladoA = -10
        area_triangulo = heron(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(area_triangulo, "Digite um triangulo valido")

    def test_area_triangulo_valido(self):
        area_triangulo = heron(self.ladoA, self.ladoB, self.ladoC)
        self.assertEqual(area_triangulo, "600.0")


class teste_triangulo_equilatero(TestCase):
    def setUp(self) -> None:
        self.lado = 12

    def test_triangulo_com_lado_invalido(self):
        self.lado = -10
        area_triangulo = area_triangulo_equilatero(self.lado)
        self.assertEqual(area_triangulo, "Digite um lado valido")

    def test_area_triangulo_valido(self):
        area_triangulo = area_triangulo_equilatero(self.lado)
        self.assertEqual(area_triangulo, "62.35")

