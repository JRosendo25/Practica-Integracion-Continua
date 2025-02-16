import unittest

from app import hola_mundo

# Clase de prueba unitaria
class TestHolaMundo(unittest.TestCase):

    # Método de prueba
    def test_hola_mundo(self):
        # Llamamos a la función y guardamos el resultado
        resultado = hola_mundo()
        
        # Verificamos que el resultado sea igual a "Hola Mundo"
        self.assertEqual(resultado, "Hola Mundo")

# Ejecutar las pruebas si este script es el principal
if __name__ == "__main__":
    unittest.main()