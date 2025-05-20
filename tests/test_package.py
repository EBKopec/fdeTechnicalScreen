import unittest
from main import Package, VOL, KILO


class TestPackage(unittest.TestCase):
    def setUp(self):
        self.side = (VOL ** (1/3)) + 1
        self.light = Package("P1", 1, 1, 1, 1)
        self.heavy = Package("P2", 1, 1, 1, KILO + 1)
        self.bulky = Package("P3", self.side, self.side, self.side, 1)
        self.both = Package("P4", self.side, self.side, self.side, KILO + 1)

    def test_is_bulky(self):
        self.assertFalse(self.light.is_bulky())
        self.assertFalse(self.heavy.is_bulky())
        self.assertTrue(self.bulky.is_bulky())
        self.assertTrue(self.both.is_bulky())

    def test_is_heavy(self):
        self.assertFalse(self.light.is_heavy())
        self.assertTrue(self.heavy.is_heavy())
        self.assertFalse(self.bulky.is_heavy())
        self.assertTrue(self.both.is_heavy())

    def test_rejected(self):
        res = self.both.rejected()
        self.assertTrue(res)

        self.assertFalse(self.light.rejected())
        self.assertFalse(self.heavy.rejected())
        self.assertFalse(self.bulky.rejected())

    def test_special(self):
        self.assertTrue(self.bulky.special())
        self.assertTrue(self.heavy.special())
        self.assertTrue(self.both.special())

    def test_standard(self):
        self.assertTrue(self.light.standard())
        self.assertFalse(self.heavy.standard())
        self.assertFalse(self.bulky.standard())
        self.assertFalse(self.both.standard())

    def test_sort(self):
        self.assertEqual(self.light.sort(), "STANDARD")
        self.assertEqual(self.heavy.sort(), "SPECIAL")
        self.assertEqual(self.bulky.sort(), "SPECIAL")
        self.assertEqual(self.both.sort(), "REJECTED")


if __name__ == '__main__':
    unittest.main()
