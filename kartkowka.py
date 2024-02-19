class Uczen:
    liczba_uczniow = 0
    @staticmethod
    def srednia(lista):
        srednia=sum(lista)/len(lista)
        return srednia
    
    def __init__(self, imie, nazwisko) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny_mat = [1, 2]
        self.srednia_ocen_mat = self.srednia(self.oceny_mat)
        self.oceny_ang = [5, 6]
        self.srednia_ocen_ang = self.srednia(self.oceny_ang)
        Uczen.liczba_uczniow += 1

    def inf(self):
        print(f"imię {self.imie}")
        print(f"nazwisko {self.nazwisko}")
        print(f"matematyka {self.oceny_mat}")
        print(f"średnia matematyka {self.srednia_ocen_mat}")
        print(f"ang {self.oceny_ang}")
        print(f"średnia ang {self.srednia_ocen_ang}")

    def policz(self, oceny):
        if len(oceny) > 0:
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
uczen1 = Uczen("Olek", "Olkowski")
uczen1.inf()
print("==="*10)
print("==="*10)
print("==="*10)
uczen1.edytuj_imie("Alex")
print("Nie ma takiej oceny na liscie")
uczen1.liczba_stworzonych_uczniow()
uczen1.inf()



class Matematyka:

    @staticmethod
    def ile_liczb_parzystych():
        count = 0
        for liczba in range(100):
            if liczba % 2 == 0:
                count += 1
        return count

    @staticmethod
    def czy_pierwsza(liczba: int):
        if liczba < 2:
            return False
        for i in range(2, int(liczba ** 0.5) + 1):
            if liczba % i == 0:
                return False
        return True

    @staticmethod
    def ile_liczb_pierwszych():
        count = 0
        for liczba in range(100):
            if Matematyka.czy_pierwsza(liczba):
                count += 1
        return count


from random import randint
liczby = [i for i in range(100)]

print("Ilość liczb parzystych:", Matematyka.ile_liczb_parzystych())
print("Ilość liczb pierwszych:", Matematyka.ile_liczb_pierwszych())
