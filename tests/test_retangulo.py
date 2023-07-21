from unittest import TestCase

from geometria.retangulo import area


class test_area_retangulo(TestCase):
    def setUp(self) -> None:
        self.base = 10
        self.altura = 20

    def test_retangulo_com_entrada_valida(self):
        area_retangulo = area(self.base, self.altura)
        self.assertEqual(area_retangulo, 200)

    def test_retangulo_entrada_invalida(self):
        self.base = 0
        area_retangulo = area(self.base, self.altura)
        self.assertEqual(area_retangulo, "Digite um valor de entrada valido")