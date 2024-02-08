from random import randint

class Uczen:
    liczba_uczniow_inf = 0

    def __init__(self, _imie, _nazwisko) -> None:
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.oceny_mat = [1,2]
        self.srednia_ocen_mat = self.oblicz_srednia(self.oceny_mat)
        self.oceny_ang = [5, 6]
        self.srednia_ocen_ang = self.oblicz_srednia(self.oceny_ang)
        Uczen.liczba_uczniow_inf += 1

    def inf(self):
        print(f"imie: {self.imie}")
        print(f"nazwisko: {self.nazwisko}")
        print(f"matematyka: {self.oceny_mat}")
        print(f"srednia matematyka: {self.srednia_ocen_mat}")
        print(f"ang: {self.oceny_ang}")
        print(f"srednia ang: {self.srednia_ocen_ang}")
        print("="*10)

    @classmethod
    def liczba_stworzonych_uczniow(cls):
        return cls.liczba_uczniow_inf

    def zmien_imie(self, nowe_imie):
        self.imie = nowe_imie

    def usun_ocene(self, ocena):
        if ocena in self.oceny_mat:
            self.oceny_mat.remove(ocena)
            self.srednia_ocen_mat = self.oblicz_srednia(self.oceny_mat)
        if ocena in self.oceny_ang:
            self.oceny_ang.remove(ocena)
            self.srednia_ocen_ang = self.oblicz_srednia(self.oceny_ang)

    def oblicz_srednia(self, oceny):
        return sum(oceny) / len(oceny) if oceny else 0

print("==="*10)
u1 = Uczen("Olek", "Olkowaty")
u1.inf()
print("==="*10)
u2 = Uczen("Alex", "Olkowaty")
u2.inf()
