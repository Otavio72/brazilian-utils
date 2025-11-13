import unittest
from brutils.boleto import generate_boleto, is_valid_boleto, format_boleto

class TestBoleto(unittest.TestCase):
    def test_generate_returns_valid(self):
        boleto = generate_boleto()
        self.assertTrue(is_valid_boleto(boleto), f"Boleto inválido: {boleto}")

    def test_formatting(self):
        boleto = generate_boleto()
        formatted = format_boleto(boleto)
        self.assertIsInstance(formatted, str)
        self.assertIn('.', formatted)
        self.assertIn(' ', formatted)

    def test_invalid_length(self):
        boleto = "123456"  # muito curto
        self.assertFalse(is_valid_boleto(boleto))

    def test_non_numeric(self):
        boleto = "12345a78901234567890123456789012345678901234567"
        self.assertFalse(is_valid_boleto(boleto))

if __name__ == "__main__":
    unittest.main()