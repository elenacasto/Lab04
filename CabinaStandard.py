class CabinaStandard:
    def __init__(self, codice, num_letti, ponte, prezzo):
        self._codice = codice
        self._num_letti = int(num_letti)
        self._ponte = int(ponte)
        self._prezzo = float(prezzo)
        self._disponibile = True
        self._passeggero = None

    @property
    def codice(self):
        return self._codice

    @property
    def prezzo(self):
        return self._prezzo

    @property
    def disponibile(self):
        return self._disponibile

    def assegna_passeggero(self, passeggero):
        self._passeggero = passeggero
        self._disponibile = False

    def __str__(self):
        stato = "Disponibile" if self._disponibile else "Occupata"
        return (f"{self._codice} : Standard | {self._num_letti} letti - Ponte {self._ponte} - "
                f"Prezzo - {self._prezzo} - {stato}")

    def __lt__(self, other):
        return self.prezzo < other.prezzo

