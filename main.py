liczba_pracownikow = int(input())
lista_pracownikow = []

class Pracownik:
		def __init__(self, imie, niby_pensja):
			self.imie = str(imie)
			self.pensja = niby_pensja

		def __repr__(self):
			return f"{self.imie} {self.pensja}"

		def suma_netto(self):
			c = (self.pensja *0.0976) + (self.pensja*0.015) + (self.pensja*0.0245)
			d = self.pensja - c
			e = d*0.09
			f = d*0.0775
			g = 111.25
			h = self.pensja - c - g
			h_2 = round(h, 0)

			i = ((h)*0.18)-46.33
			j = round(i-f, 0)
			self.netto = self.pensja - c - e - j
			return self.netto

		def suma_skladki(self):
			self.skladki = self.pensja *0.0976 + self.pensja*0.065 + self.pensja*0.0193 + self.pensja*0.0245 + self.pensja*0.001
			return round(self.skladki, 2)

		def suma_koszt(self):
			self.koszt = self.pensja + self.pensja *0.0976 + self.pensja*0.065 + self.pensja*0.0193 + self.pensja*0.0245 + self.pensja*0.001
			return round(self.koszt, 2)

		def suma_calkowity(self):
			return round((self.pensja + self.suma_skladki()), 2)

		

for i in range(0, liczba_pracownikow):
	kol = input()
	kol = kol.split()
	imie = kol[0]
	niby_pensja = int(kol[1])
	pracownik = Pracownik(imie, niby_pensja)
	lista_pracownikow.append(pracownik)

calkowity = 0
for i in range(0, liczba_pracownikow):
    imie = lista_pracownikow[i].imie
    niby_pensja = lista_pracownikow[i].pensja
    calkowity += lista_pracownikow[i].suma_calkowity()
    print(imie, f"{lista_pracownikow[i].suma_netto():.2f}", 
    	f"{lista_pracownikow[i].suma_skladki():.2f}",
    f"{lista_pracownikow[i].suma_koszt():.2f}")
print(calkowity)






