"""Testi kalkulators.py modulim."""

import unittest

from kalkulators import saskaitit


class TestKalkulators(unittest.TestCase):
    """Testu klase funkcijai saskaitit."""

    def test_saskaitit_pozitivus_skaitlus(self):
        """Pārbauda pozitīvu skaitļu saskaitīšanu."""
        self.assertEqual(saskaitit(2, 3), 6)

    def test_saskaitit_negativus_skaitlus(self):
        """Pārbauda negatīvu skaitļu saskaitīšanu."""
        self.assertEqual(saskaitit(-1, -1), -2)

    def test_saskaitit_nulli(self):
        """Pārbauda saskaitīšanu ar nulli."""
        self.assertEqual(saskaitit(10, 0), 10)


if __name__ == "__main__":
    unittest.main()