#z1
class Basic_Data:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Student(Basic_Data):
    def __init__(self, imie, nazwisko, wiek, rok):
        super().__init__(imie, nazwisko)
        if not isinstance(wiek, int):
            raise ValueError("Wiek powinien być liczbą całkowitą.")
        if not isinstance(rok, str):
            raise ValueError("Rok powinien być ciągiem znaków.")

        self.wiek = wiek
        self.rok = rok

    def information(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Wiek: {self.wiek}")
        print(f"Rok: {self.rok}")

try:
    student1 = Student("Jan", "Kowalski", 20, "3A")
    student1.information()
except ValueError as e:
    print(f"Błąd: {e}")

#z2
    
import random

class Generator_Ocen:
    def generuj_losowe_oceny(self, ilosc_ocen):
        return [random.randint(2, 5) for _ in range(ilosc_ocen)]

class Student(Basic_Data):
    def __init__(self, imie, nazwisko, wiek, rok):
        super().__init__(imie, nazwisko)
        self.wiek = wiek
        self.rok = rok
        self.generator_ocen = Generator_Ocen()
        self.oceny_z_matematyki = self.generator_ocen.generuj_losowe_oceny(5)
        self.oceny_z_fizyki = self.generator_ocen.generuj_losowe_oceny(5)

    def information(self):
        super().information()
        print(f"Wiek: {self.wiek}")
        print(f"Rok: {self.rok}")
        print(f"Oceny z matematyki: {self.oceny_z_matematyki}")
        print(f"Oceny z fizyki: {self.oceny_z_fizyki}")
try:
    student2 = Student("Anna", "Nowak", 22, "2B")
    student2.information()
except ValueError as e:
    print(f"Błąd: {e}")

#Z3
class Obliczenia:
    @staticmethod
    def srednia_arytmetyczna(oceny):
        if not oceny:
            return 0
        return sum(oceny) / len(oceny)

oceny_z_matematyki = [4, 5, 3, 4, 5]
oceny_z_fizyki = [3, 4, 4, 5, 5]

srednia_matematyka = Obliczenia.srednia_arytmetyczna(oceny_z_matematyki)
srednia_fizyka = Obliczenia.srednia_arytmetyczna(oceny_z_fizyki)

print(f"Średnia z matematyki: {srednia_matematyka}")
print(f"Średnia z fizyki: {srednia_fizyka}")
 #Z4
import math

class RownanieKwadratowe:
    @staticmethod
    def liczba_rozwiazan(a, b, c):
        delta = b**2 - 4*a*c

        if delta > 0:
            return "Równanie kwadratowe ma dwa rozwiązania."
        elif delta == 0:
            return "Równanie kwadratowe ma jedno rozwiązanie."
        else:
            return "Równanie kwadratowe nie ma rozwiązań."

a = 1
b = -3
c = 2

wynik = RownanieKwadratowe.liczba_rozwiazan(a, b, c)
print(wynik)