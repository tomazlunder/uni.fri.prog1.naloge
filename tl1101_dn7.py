def tekac(stevilka, ime, leto, h, m, s):
    return "{stevilka:4}. {ime:20} {h:02}:{m:02}:{s:02}".format(**locals())

def tekac_star(stevilka, ime, leto, h, m, s):
    ime_in_leto = "{} ({})".format(ime, leto)
    return "{:4}. {:26} {:02}:{:02}:{:02}".format(stevilka, ime_in_leto, h, m, s)

#Optimalna rešitev, ki je bila pred iztekom roka podana s strani izr. prof. dr. Janeza Demšarja


import unittest
class TestTekaci(unittest.TestCase):
    def test_tekac(self):
        self.assertEqual(tekac(1, "ROMAN SONJA", 1979, 1, 15, 2),
                         "   1. ROMAN SONJA          01:15:02")
        self.assertEqual(tekac(1234, "ROMAN SONJA", 1979, 0, 1, 23),
                         "1234. ROMAN SONJA          00:01:23")
        self.assertEqual(tekac(1, "JAN HUS", 1979, 1, 15, 2),
                         '   1. JAN HUS              01:15:02')
    def test_tekac_star(self):
        self.assertEqual(tekac_star(1, "ROMAN SONJA", 1979, 1, 15, 2),
                         "   1. ROMAN SONJA (1979)         01:15:02")
        self.assertEqual(tekac_star(1234, "ROMAN SONJA", 1979, 0, 1, 23),
                         "1234. ROMAN SONJA (1979)         00:01:23")
        self.assertEqual(tekac_star(1234, "JAN HUS", 1979, 0, 1, 23),
                         '1234. JAN HUS (1979)             00:01:23')

if __name__ == "__main__":
    unittest.main()
