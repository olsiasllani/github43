# nxenesi.py

class Nxenesi:
    def __init__(self, emri):
        self.emri = emri
        self.projekti_perfunduar = False

    def perfundoni_projektin(self):
        """Nxënësi përfundon projektin dhe mund të marrë certifikatën."""
        self.projekti_perfunduar = True
        print(f"{self.emri} ka përfunduar projektin!")
