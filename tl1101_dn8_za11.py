from itertools import product
from collections import *
#Ogrevalne naloge
def visina(plosca):
    return len(plosca)

def sirina(plosca):
    for vrsta in plosca:
        return len(vrsta)

def polj(plosca):
    vsota = 0
    for vrsta in plosca:
        vsota += len(vrsta)
    return vsota

def na_plosci(plosca, x, y):
    return -1<y<= visina(plosca)-1 and -1<x<= sirina(plosca)-1

def preberi(plosca, x, y):
    skupaj = plosca[y][x]
    return (skupaj[0], int(skupaj[1:]))

#Za 6
def premakni(plosca, x, y):
    začetna = preberi(plosca, x, y)
    if začetna[0] == "V":
        return(x+začetna[1], y)
    if začetna[0] == "Z":
        return(x-začetna[1], y)
    if začetna[0] == "S":
        return(x, y-začetna[1])
    if začetna[0] == "J":
        return(x, y+začetna[1])

def dolzina_poti(plosca, x, y):
    i = 0
    while na_plosci(plosca, x, y):
        xiny = premakni(plosca, x, y)
        x, y = xiny[0], xiny[1]
        i +=1
    return i

#Za 7
def pot(plosca, x, y):
    seznam = []
    seznam.append((x, y))
    while na_plosci(plosca, x, y):
        xiny = premakni(plosca, x, y)
        x, y = xiny[0], xiny[1]
        seznam.append(xiny)
    return seznam[:-1]

#Za 8
def ciklicno(plosca, x, y):
    i = 0
    while na_plosci(plosca, x, y) and i<20:
        xiny = premakni(plosca, x, y)
        x, y = xiny[0], xiny[1]
        i +=1
    return False if i<20 else True

def ciklicna(plosca):
    xlista = range(0, sirina(plosca))
    ylista = range(0, visina(plosca))
    mnozica = set()
    for koordinati in product(xlista, ylista):
        x = koordinati[0]
        y = koordinati[1]
        if ciklicno(plosca, x, y):
            mnozica.add((x, y))
    return mnozica

def vrnljivo(plosca, x, y):
    seznam = []
    x1, y1 = x, y
    i = 0
    while na_plosci(plosca, x1, y1) and i<20:
        x1_in_y1 = premakni(plosca, x1, y1)
        x1, y1 = x1_in_y1[0], x1_in_y1[1]
        seznam.append(x1_in_y1)
        i += 1
    return True if (x, y) in seznam else False

def vrnljiva(plosca):
    xlista = range(0, sirina(plosca))
    ylista = range(0, visina(plosca))
    mnozica = set()
    for polje in product(xlista, ylista):
        x = polje[0]
        y = polje[1]
        if vrnljivo(plosca, x, y):
            mnozica.add((x, y))
    return mnozica

def varno(plosca, x, y):
    prvi_korak = premakni(plosca, x, y)
    x1, y1 = prvi_korak[0], prvi_korak[1]
    return True if na_plosci(plosca, x1, y1) else False

def varna(plosca):
    xlista = range(0, sirina(plosca))
    ylista = range(0, visina(plosca))
    mnozica = set()
    for polje in product(xlista, ylista):
        x = polje[0]
        y = polje[1]
        if varno(plosca, x, y):
            mnozica.add((x, y))
    return mnozica

#Za 9
def dolzina_cikla(plosca, x, y):
    if ciklicno(plosca, x, y):
        x1, y1 = premakni(plosca, x, y)
        x2, y2 = premakni(plosca, x1, y1)
        c = 1
        while x1 != x2 or y1 != y2:
            x2, y2 = premakni(plosca, x2, y2)
            c += 1
        return c
    else:
        return None

def veckratnik_ciklov(plosca):
    mn_cik = ciklicna(plosca)
    lista = []
    for e in mn_cik:
        x, y = e[0], e[1]
        lista.append(dolzina_cikla(plosca, x, y))
    while len(lista)>1:
        prvi, drugi = lista[0], lista[1]
        lista.pop(0)
        lista.pop(0)
        lista.append(najmanjsi_skupni(prvi, drugi))
        #Dokončaj
    if len(lista) == 0:
        return 1
    return lista[0]

#Iskalnik najmanjšega skupnega večkratnika
def najmanjsi_skupni(x, y):
    n = 1
    while (x*n)%y != 0:
        n +=1
    return n*x

#Za 10 in 11 :)
def igra(plosca, zacetki):
    #Naredi slovar oblike št: (x,y)
    slovar = defaultdict()
    for st, koordinati in enumerate(zacetki):
        slovar[st] = koordinati

    #Ključe slovarja spravi v seznam, če je samo en zmaga ^^
    indeksi = sorted(slovar.keys())
    if len(indeksi) == 1:
        return indeksi[0]

    #While zanka izvaja runde igre
    turn = 0
    po_vrsti = [] #Od desne proti levi
    while len(indeksi) > 1 and turn <20:
        for igralec in indeksi:
            if slovar[igralec] == (999,999):
                del slovar[igralec]
                po_vrsti.append(igralec)
                indeksi.remove(igralec)
        for igralec in indeksi:
            if slovar[igralec] != (999,999):
                x, y = slovar[igralec]
                slovar[igralec] = premakni(plosca, x, y)
                for drugi_igralci in indeksi:
                    if indeksi.index(igralec) != indeksi.index(drugi_igralci) and slovar[igralec] == slovar[drugi_igralci]:
                        slovar[drugi_igralci] = (999,999)
        for igralec in indeksi:
            x1, y1 = slovar[igralec]
            if not na_plosci(plosca, x1, y1):
                slovar[igralec] = (999,999)
        turn += 1

    #Da vidimo kdo je zmagovalec
    if len(indeksi) > 1:
        return set(indeksi)
    if len(indeksi) == 1:
        po_vrsti.append(indeksi[0])
        return po_vrsti[len(po_vrsti)-1]

#TESTI
import unittest
class TestOcena05(unittest.TestCase):
    def test_visina(self):
        self.assertEqual(visina([["V1", "V1"],
                                 ["V2", "V2"],
                                 ["V3", "V3"]]), 3)

        self.assertEqual(visina([["V1", "V1"],
                                 ["V2", "V2"],
                                 ["V3", "V3"],
                                 ["V4", "V4"],
                                 ["V4", "V4"]]), 5)

        self.assertEqual(visina([["V1", "V1", "V1", "V1", "V1"]]), 1)

        self.assertEqual(visina([["V1"]]), 1)

    def test_sirina(self):
        self.assertEqual(sirina([["V1", "V1"],
                                 ["V2", "V2"],
                                 ["V3", "V3"]]), 2)

        self.assertEqual(sirina([["V1", "V1"],
                                 ["V2", "V2"],
                                 ["V3", "V3"],
                                 ["V4", "V4"],
                                 ["V4", "V2"]]), 2)

        self.assertEqual(sirina([["V1", "V1", "V1", "V1", "V1"]]), 5)

        self.assertEqual(sirina([["V1", "V1", "V1", "V1", "V1"],
                                 ["V2", "V2", "V2", "V2", "V2"]]), 5)

        self.assertEqual(sirina([["V1", "V2", "V3", "V4", "V5"]]), 5)

        self.assertEqual(sirina([["V1"]]), 1)

    def test_polj(self):
        self.assertEqual(polj([["V1", "V1"],
                               ["V2", "V2"],
                               ["V3", "V3"]]), 6)

        self.assertEqual(polj([["V1", "V1"],
                               ["V2", "V2"],
                               ["V3", "V3"],
                               ["V4", "V4"],
                               ["V4", "V2"]]), 10)

        self.assertEqual(polj([["V1", "V1", "V1", "V1", "V1"]]), 5)

        self.assertEqual(polj([["V1", "V1", "V1", "V1", "V1"],
                               ["V2", "V2", "V2", "V2", "V2"]]), 10)

        self.assertEqual(polj([["V1", "V2", "V3", "V4", "V5"]]), 5)

        self.assertEqual(polj([["V1"]]), 1)

    def test_na_plosci(self):
        plosca = [["V1", "V1"],
                  ["V2", "V2"],
                  ["V3", "V3"]]
        self.assertTrue(na_plosci(plosca, 0, 0))
        self.assertTrue(na_plosci(plosca, 1, 0))
        self.assertTrue(na_plosci(plosca, 0, 1))
        self.assertTrue(na_plosci(plosca, 1, 2))

        self.assertFalse(na_plosci(plosca, 0, 3))
        self.assertFalse(na_plosci(plosca, 2, 0))

        self.assertFalse(na_plosci(plosca, 1, 5))
        self.assertFalse(na_plosci(plosca, 1, -5))
        self.assertFalse(na_plosci(plosca, -10, -5))
        self.assertFalse(na_plosci(plosca, 10, 5))
        self.assertFalse(na_plosci(plosca, -10, 0))

        plosca = [["V1"] * 5] * 12
        self.assertTrue(na_plosci(plosca, 4, 11))
        self.assertTrue(na_plosci(plosca, 0, 0))
        self.assertFalse(na_plosci(plosca, 5, 11))
        self.assertFalse(na_plosci(plosca, 4, 12))
        self.assertFalse(na_plosci(plosca, 5, 12))
        self.assertFalse(na_plosci(plosca, -1, -1))


    def test_preberi(self):
        plosca = [["J2", "Z12", "J1"],
                  ["V2", "V1", "S2"],
                  ["S1", "J1345", "S1"]]
        self.assertEqual(preberi(plosca, 0, 1), ("V", 2))
        self.assertEqual(preberi(plosca, 2, 1), ("S", 2))
        self.assertEqual(preberi(plosca, 0, 2), ("S", 1))
        self.assertEqual(preberi(plosca, 1, 0), ("Z", 12))
        self.assertEqual(preberi(plosca, 1, 2), ("J", 1345))

class Plosce(unittest.TestCase):
    def setUp(self):
        self.plosca1 = [["J2", "Z1", "J1"],
                        ["V2", "V1", "S2"],
                        ["S1", "Z1", "S1"]]

        self.plosca2 = [["J2", "Z1", "V1"],
                        ["S1", "V1", "J1"],
                        ["S1", "S1", "Z1"]]

        self.plosca3 = [["J1", "J2"],
                        ["J1", "V1"],
                        ["S1", "S1"]]

        self.plosca4 = [["V2", "V1", "Z1", "J1"]]

        self.plosca5 = [["J2"], ["J1"], ["S1"], ["V1"]]

        self.vsa = {(x, y) for x in range(3) for y in range(3)}

class TestOcena06(Plosce):
    def test_premakni(self):
        plosca = [["J2", "Z12", "J1"],
                  ["V2", "V1", "S2"],
                  ["S1", "J1345", "S1"]]
        self.assertTupleEqual(premakni(plosca, 0, 0), (0, 2))
        self.assertTupleEqual(premakni(plosca, 1, 0), (-11, 0))
        self.assertTupleEqual(premakni(plosca, 2, 0), (2, 1))
        self.assertTupleEqual(premakni(plosca, 0, 1), (2, 1))
        self.assertTupleEqual(premakni(plosca, 1, 1), (2, 1))
        self.assertTupleEqual(premakni(plosca, 2, 1), (2, -1))
        self.assertTupleEqual(premakni(plosca, 0, 2), (0, 1))
        self.assertTupleEqual(premakni(plosca, 1, 2), (1, 1347))
        self.assertTupleEqual(premakni(plosca, 2, 2), (2, 1))

    def test_dolzina_poti(self):
        plosca = self.plosca1
        self.assertEqual(dolzina_poti(plosca, 0, 0), 4)
        self.assertEqual(dolzina_poti(plosca, 1, 0), 5)
        self.assertEqual(dolzina_poti(plosca, 2, 0), 2)
        self.assertEqual(dolzina_poti(plosca, 0, 1), 2)
        self.assertEqual(dolzina_poti(plosca, 1, 1), 2)
        self.assertEqual(dolzina_poti(plosca, 2, 1), 1)
        self.assertEqual(dolzina_poti(plosca, 0, 2), 3)
        self.assertEqual(dolzina_poti(plosca, 1, 2), 4)
        self.assertEqual(dolzina_poti(plosca, 2, 2), 2)

        plosca = [["J2", "Z1"]]
        self.assertEqual(dolzina_poti(plosca, 0, 0), 1)
        self.assertEqual(dolzina_poti(plosca, 1, 0), 2)

        self.assertEqual(dolzina_poti([["Z2"]], 0, 0), 1)


class TestOcena07(Plosce):
    def test_pot(self):
        potl = lambda *x: list(pot(*x))

        plosca = self.plosca1
        self.assertEqual(potl(plosca, 0, 0), [(0, 0), (0, 2), (0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 1, 0), [(1, 0), (0, 0), (0, 2), (0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 2, 0), [(2, 0), (2, 1)])
        self.assertEqual(potl(plosca, 0, 1), [(0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 1, 1), [(1, 1), (2, 1)])
        self.assertEqual(potl(plosca, 2, 1), [(2, 1)])
        self.assertEqual(potl(plosca, 0, 2), [(0, 2), (0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 1, 2), [(1, 2), (0, 2), (0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 2, 2), [(2, 2), (2, 1)])

        plosca = [["J2", "Z1"]]
        self.assertEqual(potl(plosca, 0, 0), [(0, 0)])
        self.assertEqual(potl(plosca, 1, 0), [(1, 0), (0, 0)])

        self.assertEqual(potl([["Z2"]], 0, 0), [(0, 0)])


class TestOcena08(Plosce):
    def test_ciklicno(self):
        for x in range(3):
            for y in range(3):
                self.assertFalse(ciklicno(self.plosca1, x, y))
                if (x, y) != (2, 0):
                    self.assertTrue(ciklicno(self.plosca2, x, y))
        self.assertFalse(ciklicno(self.plosca2, 2, 0))

        self.assertTrue(ciklicno(self.plosca3, 0, 0))
        self.assertTrue(ciklicno(self.plosca3, 0, 1))
        self.assertTrue(ciklicno(self.plosca3, 0, 2))
        self.assertFalse(ciklicno(self.plosca3, 1, 0))
        self.assertFalse(ciklicno(self.plosca3, 1, 1))
        self.assertFalse(ciklicno(self.plosca3, 1, 2))

        self.assertTrue(ciklicno(self.plosca4, 0, 0))
        self.assertTrue(ciklicno(self.plosca4, 1, 0))
        self.assertTrue(ciklicno(self.plosca4, 2, 0))
        self.assertFalse(ciklicno(self.plosca4, 3, 0))

        self.assertTrue(ciklicno(self.plosca5, 0, 0))
        self.assertTrue(ciklicno(self.plosca5, 0, 1))
        self.assertTrue(ciklicno(self.plosca5, 0, 2))
        self.assertFalse(ciklicno(self.plosca5, 0, 3))

    def test_ciklicna(self):
        self.assertSetEqual(ciklicna(self.plosca1), set())
        self.assertSetEqual(ciklicna(self.plosca2), self.vsa - {(2, 0)})
        self.assertSetEqual(ciklicna(self.plosca3), {(0, 0), (0, 1), (0, 2)})
        self.assertSetEqual(ciklicna(self.plosca4), {(0, 0), (1, 0), (2, 0)})
        self.assertSetEqual(ciklicna(self.plosca5), {(0, 0), (0, 1), (0, 2)})

    def test_vrnljivo(self):
        for x in range(3):
            for y in range(3):
                self.assertFalse(vrnljivo(self.plosca1, x, y))
                if (x, y) not in {(1, 0), (2, 0)}:
                    self.assertTrue(vrnljivo(self.plosca2, x, y))
                else:
                    self.assertFalse(vrnljivo(self.plosca2, x, y))
        self.assertFalse(vrnljivo(self.plosca3, 0, 0))
        self.assertTrue(vrnljivo(self.plosca3, 0, 1))
        self.assertTrue(vrnljivo(self.plosca3, 0, 2))
        self.assertFalse(vrnljivo(self.plosca3, 1, 0))
        self.assertFalse(vrnljivo(self.plosca3, 1, 1))
        self.assertFalse(vrnljivo(self.plosca3, 1, 2))

        self.assertFalse(vrnljivo(self.plosca4, 0, 0))
        self.assertTrue(vrnljivo(self.plosca4, 1, 0))
        self.assertTrue(vrnljivo(self.plosca4, 2, 0))
        self.assertFalse(vrnljivo(self.plosca4, 3, 0))

        self.assertFalse(vrnljivo(self.plosca5, 0, 0))
        self.assertTrue(vrnljivo(self.plosca5, 0, 1))
        self.assertTrue(vrnljivo(self.plosca5, 0, 2))
        self.assertFalse(vrnljivo(self.plosca5, 0, 3))

    def test_vrnljiva(self):
        self.assertSetEqual(vrnljiva(self.plosca1), set())
        self.assertSetEqual(vrnljiva(self.plosca2), self.vsa - {(1, 0), (2, 0)})
        self.assertSetEqual(vrnljiva(self.plosca3), {(0, 1), (0, 2)})
        self.assertSetEqual(vrnljiva(self.plosca4), {(1, 0), (2, 0)})
        self.assertSetEqual(vrnljiva(self.plosca5), {(0, 1), (0, 2)})

    def test_varno(self):
        for x in range(3):
            for y in range(3):
                if (x, y) != (2, 1):
                    self.assertTrue(varno(self.plosca1, x, y))
                if (x, y) != (2, 0):
                    self.assertTrue(varno(self.plosca2, x, y))
        self.assertFalse(varno(self.plosca1, 2, 1))
        self.assertFalse(varno(self.plosca2, 2, 0))

    def test_varna(self):
        self.assertSetEqual(varna(self.plosca1), self.vsa - {(2, 1)})
        self.assertSetEqual(varna(self.plosca2), self.vsa - {(2, 0)})
        self.assertSetEqual(varna(self.plosca3),
                            {(0, 0), (1, 0), (0, 1), (0, 2), (1, 2)})
        self.assertSetEqual(varna(self.plosca4), {(0, 0), (1, 0), (2, 0)})
        self.assertSetEqual(varna(self.plosca5), {(0, 0), (0, 1), (0, 2)})


class TestOcena_09(Plosce):
    def test_dolzina_cikla(self):
        for x in range(3):
            for y in range(3):
                self.assertIsNone(dolzina_cikla(self.plosca1, x, y))
                if x == 0 or (x, y) == (1, 0):
                    self.assertEqual(dolzina_cikla(self.plosca2, x, y), 3)
                elif (x, y) == (2, 0):
                    self.assertIsNone(dolzina_cikla(self.plosca2, x, y))
                else:
                    self.assertEqual(dolzina_cikla(self.plosca2, x, y), 4)

        self.assertEqual(dolzina_cikla(self.plosca3, 0, 0), 2)
        self.assertEqual(dolzina_cikla(self.plosca3, 0, 1), 2)
        self.assertEqual(dolzina_cikla(self.plosca3, 0, 2), 2)
        self.assertIsNone(dolzina_cikla(self.plosca3, 1, 0))
        self.assertIsNone(dolzina_cikla(self.plosca3, 1, 1))
        self.assertIsNone(dolzina_cikla(self.plosca3, 1, 2))

        self.assertEqual(dolzina_cikla(self.plosca4, 0, 0), 2)
        self.assertEqual(dolzina_cikla(self.plosca4, 1, 0), 2)
        self.assertEqual(dolzina_cikla(self.plosca4, 2, 0), 2)
        self.assertIsNone(dolzina_cikla(self.plosca4, 3, 0))

        self.assertEqual(dolzina_cikla(self.plosca5, 0, 0), 2)
        self.assertEqual(dolzina_cikla(self.plosca5, 0, 1), 2)
        self.assertEqual(dolzina_cikla(self.plosca5, 0, 2), 2)
        self.assertIsNone(dolzina_cikla(self.plosca5, 0, 3))

    def test_veckratnik_ciklov(self):
        self.assertEqual(veckratnik_ciklov(self.plosca1), 1)
        self.assertEqual(veckratnik_ciklov(self.plosca2), 12)
        self.assertEqual(veckratnik_ciklov(self.plosca3), 2)
        self.assertEqual(veckratnik_ciklov(self.plosca4), 2)
        self.assertEqual(veckratnik_ciklov(self.plosca5), 2)


class TestOcena_10(Plosce):
    def test_igra(self):
        # samo en igralec / single player
        self.assertTrue(igra(self.plosca1, [(2, 0)]) in [0, {0}])

        # prvi izloci drugega, se preden se le-ta premakne
        # the first eliminates the second even before the latter moves
        self.assertTrue(igra(self.plosca1, [(1, 0), (0, 0)]) in [0, {0}])

        # drugi "izloci" prvega  / the second removes the first
        self.assertTrue(igra(self.plosca1, [(2, 0), (2, 2)]) in [1, {1}])
        self.assertTrue(igra(self.plosca1, [(2, 2), (2, 0)]) in [1, {1}])

        # tisti, ki so blizje, padejo cez rob
        # those closer to the path fall off the board
        self.assertTrue(
            igra(self.plosca1, [(0, 2), (2, 2), (2, 0)]) in [0, {0}])
        self.assertTrue(
            igra(self.plosca1, [(2, 2), (0, 2), (2, 0)]) in [1, {1}])
        self.assertTrue(
            igra(self.plosca1, [(2, 2), (2, 0), (0, 2)]) in [2, {2}])

        # drugi "izloci" prvega  / the second removes the first
        self.assertTrue(igra(self.plosca2, [(0, 1), (1, 0)]) in [1, {1}])
        self.assertTrue(igra(self.plosca2, [(1, 0), (0, 1)]) in [1, {1}])

        # drugi "izloci" prvega, eden pa pade čez
        # the second removes the first, and one falls off
        self.assertTrue(
            igra(self.plosca2, [(1, 0), (0, 1), (2, 0)]) in [1, {1}])
        self.assertTrue(
            igra(self.plosca2, [(2, 0), (1, 0), (0, 1)]) in [2, {2}])

        self.assertTrue(igra(self.plosca3, [(0, 0), (0, 1)]) in [0, {0}])
        self.assertTrue(igra(self.plosca3, [(0, 1), (0, 0)]) in [0, {0}])
        self.assertTrue(igra(self.plosca3, [(0, 1), (0, 2)]) in [0, {0}])
        self.assertTrue(igra(self.plosca3, [(0, 2), (0, 1)]) in [0, {0}])
        self.assertTrue(igra(self.plosca3, [(0, 2), (0, 0)]) in [1, {1}])
        self.assertTrue(igra(self.plosca3, [(0, 0), (0, 2)]) in [1, {1}])

        self.assertTrue(
            igra(self.plosca3, [(0, 0), (0, 2), (1, 0)]) in [1, {1}])
        self.assertTrue(
            igra(self.plosca3, [(0, 0), (1, 0), (0, 2)]) in [2, {2}])
        self.assertTrue(
            igra(self.plosca3, [(1, 0), (0, 0), (0, 2)]) in [2, {2}])

class TestOcena_11(Plosce):
    def test_igra(self):
        self.assertSetEqual(
            igra(self.plosca2, [(1, 0), (0, 1), (2, 0), (2, 2)]),
            {1, 3})
        self.assertSetEqual(
            igra(self.plosca2, [(1, 0), (0, 1), (2, 0), (2, 2), (1, 2)]),
            {1, 3})
        self.assertSetEqual(
            igra(self.plosca2, [(1, 0), (0, 1), (2, 0), (2, 2), (1, 2), (1, 1)]),
            {1, 3, 5})
        self.assertSetEqual(
            igra(self.plosca2, [(1, 1), (2, 1), (2, 2), (1, 2)]),
            {0, 2})

if __name__ == "__main__":
    unittest.main()
