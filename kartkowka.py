class Uczen:
    liczba_uczniow = 0
    def __init__(self, imie, nazwisko) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny_mat = [2,3,4,5,6]
        self.srednia_ocen_mat = 0
        self.oceny_ang = [5,6,6,6,6,6,6,6]
        self.srednia_ocen_ang = 0
        Uczen.liczba_uczniow += 1

    def inf(self):
        print(f"imię {self.imie}")
        print(f"nazwisko {self.nazwisko}")
        print(f"matematyka {self.oceny_mat}")
        print(f"średnia matematyka {self.srednia_ocen_mat}")
        print(f"ang {self.oceny_ang}")
        print(f"średnia ang {self.srednia_ocen_ang}")

    def policz(self, oceny):
        if len(oceny) >0:
            return sum(oceny)/len(oceny)
        else:
            return 0

    @classmethod
    def liczba_stworzonych_uczniow(cls):
        print(cls.liczba_uczniow)

    def edytuj_imie(self, nowe_imie):
        self.imie = nowe_imie

    def usun_szóstki(self, szóstki_z_matmy, szóstki_z_angola):
        self.oceny_mat = szóstki_z_matmy
        self.oceny_ang = szóstki_z_angola

print("==="*10)
print("==="*10)
uczen1 = Uczen("Adrianek", "Poniatowski")
uczen1.inf()
print("==="*10)
print("==="*10)
print("==="*10)
uczen1.edytuj_imie("Alex")
uczen1.usun_szóstki([2,3,4,5], [5])
uczen1.liczba_stworzonych_uczniow()
uczen1.inf()
print("Liczba stworzonych uczniów:", Uczen.liczba_stworzonych_uczniow())
