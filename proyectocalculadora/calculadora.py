from sumar import Sumar
from restar import Restar
from dividir import Dividir
from multiplicar import Multiplicar
from sumar_multiples import SumarMultiples

class Calculadora(Sumar, Restar, Dividir, Multiplicar, SumarMultiples):
    def __init__(self):
        pass