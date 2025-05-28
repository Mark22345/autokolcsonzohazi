from autokolcsonzo import Autokolcsonzo
from auto import Szemelyauto, Teherauto

def elokeszitett_adatok():
    kolcsonzo = Autokolcsonzo("GDE Autókölcsönző")
    kolcsonzo.autok_hozzaadasa(Szemelyauto("NVX592", "Volskwagen Golf GTI V", 10000, 5))
    kolcsonzo.autok_hozzaadasa(Teherauto("MPV592", "Volvo FH16", 15000, 1200))
    kolcsonzo.autok_hozzaadasa(Szemelyauto("JKL874", "Ford Cmax", 9000, 4))

    kolcsonzo.berles_hozzaadasa("NVX592", "2025-03-01")
    kolcsonzo.berles_hozzaadasa("MPV592", "2025-04-02")
    kolcsonzo.berles_hozzaadasa("JKL874", "2025-05-03")
    kolcsonzo.berles_hozzaadasa("NVX592", "2025-06-04")

    return kolcsonzo

def main():
    kolcsonzo = elokeszitett_adatok()S

    while True:
        print("\n--- Autókölcsönző ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("0. Kilépés")

        valasz = input("Választás: ")

        if valasz == "1":
            rendszam = input("Rendszám: ")
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            ar = kolcsonzo.berles_hozzaadasa(rendszam, datum)
            if ar:
                print(f"Bérlés sikeres. Ár: {ar} Ft")
            else:
                print("A bérlés nem lehetséges (foglalva vagy nem létezik).")

        elif valasz == "2":
            rendszam = input("Rendszám: ")
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            if kolcsonzo.berles_lemondasa(rendszam, datum):
                print("Bérlés sikeresen lemondva.")
            else:
                print("Nem található ilyen bérlés.")

        elif valasz == "3":
            print("\nAktuális bérlések:")
            for b in kolcsonzo.listaz_berlesek():
                print(b)

        elif valasz == "0":
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
