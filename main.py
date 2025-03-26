# main.py
from kursi import Kursi
from nxenesi import Nxenesi


def main() :
    # Krijo një kurs të ri
    kursi_programimit = Kursi("Programim i avancuar", "Ky kurs mëson teknika të avancuara të programimit.",
                              "Krijimi i një aplikacioni Python")

    # Krijo disa nxënës
    nxenesi1 = Nxenesi("Ali")
    nxenesi2 = Nxenesi("Besa")
    nxenesi3 = Nxenesi("Drita")

    # Regjistro nxënësit në kurs
    kursi_programimit.regjistro_nxenes(nxenesi1)
    kursi_programimit.regjistro_nxenes(nxenesi2)
    kursi_programimit.regjistro_nxenes(nxenesi3)

    # Nxënësi 1 dhe 2 përfundojnë projektin
    nxenesi1.perfundoni_projektin()
    nxenesi2.perfundoni_projektin()

    # Verifikojmë nëse nxënësit kanë përfunduar projektin dhe mund të marrin certifikatën
    kursi_programimit.kontrollo_perfundimin_projekti(nxenesi1)  # Nxënësi 1 duhet të marrë certifikatën
    kursi_programimit.kontrollo_perfundimin_projekti(nxenesi2)  # Nxënësi 2 duhet të marrë certifikatën
    kursi_programimit.kontrollo_perfundimin_projekti(nxenesi3)  # Nxënësi 3 nuk ka përfunduar projektin


if __name__ == "__main__" :
   main()
