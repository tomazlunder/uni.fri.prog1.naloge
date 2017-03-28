def starost_starsa(oseba):
    najstarejši = 0
    for otrok in rodbina[oseba]:
        if starost[otrok] > najstarejši:
            najstarejši = starost[otrok]
    if najstarejši == 0:
        return 999
    else:
        return starost[oseba]-najstarejši

def najmlajsi_stars(oseba):
    if otroci(oseba):
        prvo_rojstvo = starost_starsa(oseba)
        for otrok in otroci(oseba):
            prvo_rojstvo_otroka = najmlajsi_stars(otrok)
            if prvo_rojstvo_otroka < prvo_rojstvo:
                prvo_rojstvo = prvo_rojstvo_otroka
    else:
        return 999
    return prvo_rojstvo

def starsi_pred(oseba, n):
    množica = set()
    if otroci(oseba):
        prvo_rojstvo = starost_starsa(oseba)
        if prvo_rojstvo < n:
            množica.add(oseba)
        for otrok in otroci(oseba):
            množica = množica | set(starsi_pred(otrok, n))
    else:
        return set()
    return množica

def ime_najml_starsa(oseba):
    if otroci(oseba):
        lista = potomci(oseba)
        naj_lista = []
        naj_starost = 999
        for oseba in lista:
            if starost_starsa(oseba) < naj_starost:
                naj_starost = starost_starsa(oseba)
                naj_lista = [oseba]
            elif starost_starsa(oseba) == naj_starost:
                naj_lista.append(oseba)
        return sorted(naj_lista)[0]
    else:
        return None

def potomci(oseba):
    if otroci(oseba):
        lista_imen =[oseba]
        for otrok in otroci(oseba):
            lista_imen += potomci(otrok)
        return lista_imen
    else:
        return []

# --- TESTI and stuff---

rodbina = {
        "Kajn": ["Adam"],
        "Adam": ["Matjaž", "Cilka", "Daniel", "Erik"],
        "Aleksander": [],
        "Alenka": [],
        "Barbara": [],
        "Cilka": [],
        "Daniel": ["Elizabeta", "Hans"],
        "Erik": [],
        "Elizabeta": ["Ludvik", "Jurij", "Barbara", "Herman"],
        "Franc": [],
        "Herman": ["Margareta"],
        "Hans": [],
        "Jožef": ["Alenka", "Aleksander", "Petra"],
        "Jurij": ["Franc", "Jožef"],
        "Ludvik": [],
        "Margareta": [],
        "Matjaž": ["Viljem"],
        "Mihael": [],
        "Petra": [],
        "Tadeja": [],
        "Viljem": ["Tadeja"],
    }


def otroci(oseba):
    return rodbina[oseba]

starost = {
    "Kajn": 140,
    "Adam": 111, "Matjaž": 90, "Cilka": 88, "Daniel": 85, "Erik": 83,
    "Viljem": 58, "Tadeja": 20, "Elizabeta": 67, "Hans": 64, "Ludvik": 50,
    "Jurij": 49, "Barbara": 45, "Herman": 39, "Mihael": 32, "Franc": 30,
    "Jožef": 29, "Margareta": 3, "Alenka": 9, "Aleksander": 5, "Petra": 7}


import unittest
from unittest import mock
class TestOgrevanje(unittest.TestCase):
    def test_starost_starsa(self):
        self.assertEqual(starost_starsa("Adam"), 21)
        self.assertEqual(starost_starsa("Daniel"), 18)
        self.assertEqual(starost_starsa("Elizabeta"), 17)
        self.assertEqual(starost_starsa("Herman"), 36)
        self.assertEqual(starost_starsa("Jožef"), 20)
        self.assertEqual(starost_starsa("Jurij"), 19)
        self.assertEqual(starost_starsa("Matjaž"), 32)
        self.assertEqual(starost_starsa("Viljem"), 38)

        self.assertEqual(starost_starsa("Aleksander"), 999)
        self.assertEqual(starost_starsa("Alenka"), 999)
        self.assertEqual(starost_starsa("Barbara"), 999)
        self.assertEqual(starost_starsa("Cilka"), 999)
        self.assertEqual(starost_starsa("Erik"), 999)
        self.assertEqual(starost_starsa("Franc"), 999)
        self.assertEqual(starost_starsa("Hans"), 999)
        self.assertEqual(starost_starsa("Ludvik"), 999)
        self.assertEqual(starost_starsa("Margareta"), 999)
        self.assertEqual(starost_starsa("Mihael"), 999)
        self.assertEqual(starost_starsa("Petra"), 999)
        self.assertEqual(starost_starsa("Tadeja"), 999)

    def test_najmlajsi_stars(self):
        self.assertEqual(najmlajsi_stars("Kajn"), 17)
        self.assertEqual(najmlajsi_stars("Adam"), 17)
        self.assertEqual(najmlajsi_stars("Daniel"), 17)
        self.assertEqual(najmlajsi_stars("Elizabeta"), 17)
        self.assertEqual(najmlajsi_stars("Jurij"), 19)
        self.assertEqual(najmlajsi_stars("Jožef"), 20)
        self.assertEqual(najmlajsi_stars("Alenka"), 999)
        self.assertEqual(najmlajsi_stars("Matjaž"), 32)
        self.assertEqual(najmlajsi_stars("Viljem"), 38)
        self.assertEqual(najmlajsi_stars("Tadeja"), 999)

        global najmlajsi_stars
        najmlajsi_stars = mock.Mock(wraps=najmlajsi_stars)
        najmlajsi_stars("Kajn")
        self.assertEqual(
            len([x for x in najmlajsi_stars.call_args_list if x[0][0] == "Elizabeta"]), 1,
            "Klic najmlajsi_stars('Elizabeta') se mora zgoditi natančno enkrat")


class TestObvezna(unittest.TestCase):
    def test_starsi_pred(self):
        self.assertEqual(starsi_pred("Adam", 20),
                         {"Daniel", "Elizabeta", "Jurij"})
        self.assertEqual(starsi_pred("Daniel", 20),
                         {"Daniel", "Elizabeta", "Jurij"})
        self.assertEqual(starsi_pred("Elizabeta", 20), {"Elizabeta", "Jurij"})
        self.assertEqual(starsi_pred("Jurij", 20), {"Jurij"})

        self.assertEqual(starsi_pred("Adam", 16), set())

        self.assertEqual(starsi_pred("Adam", 50),
                         {"Adam", "Matjaž", "Viljem", "Daniel", "Elizabeta",
                          "Jurij", "Herman", "Jožef"})


class TestDodatna(unittest.TestCase):
    def test_ime_najml_stars(self):
        self.assertEqual(ime_najml_starsa("Kajn"), "Elizabeta")
        self.assertEqual(ime_najml_starsa("Adam"), "Elizabeta")
        self.assertEqual(ime_najml_starsa("Daniel"), "Elizabeta")
        self.assertEqual(ime_najml_starsa("Elizabeta"), "Elizabeta")
        self.assertEqual(ime_najml_starsa("Jurij"), "Jurij")
        self.assertEqual(ime_najml_starsa("Jožef"), "Jožef")
        self.assertEqual(ime_najml_starsa("Alenka"), None)
        self.assertEqual(ime_najml_starsa("Matjaž"), "Matjaž")
        self.assertEqual(ime_najml_starsa("Viljem"), "Viljem")
        self.assertEqual(ime_najml_starsa("Tadeja"), None)
