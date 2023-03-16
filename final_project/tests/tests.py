import unittest
from translator import french_to_english, english_to_french


class TestTranslation(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('hello'), 'Bonjour')
        self.assertEqual(english_to_french(''), 'Invalid input')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(''), 'Invalid input')

if __name__ == '__main__':
    unittest.main()
