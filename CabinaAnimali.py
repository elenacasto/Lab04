class CabinaAnimali:
    def __init__(self, codice, num_letti, ponte, prezzo, max_animali):
        self._codice = codice
        self._num_letti = int(num_letti)
        self._ponte = int(ponte)
        self._prezzo = float(prezzo)
        self._max_animali = int(max_animali)
        self._disponibile = True
        self._passeggero = None

    def prezzo(self):
        return self._prezzo * (1 + 0.10 * self._max_animali)

    def __repr__(self):
        stato = "Disponibile" if self._disponibile else "Occupata"
        return f"{self._codice} : Animali | {self._num_letti} letti - Ponte {self._ponte} - Prezzo - {self._prezzo} - Max animali: {self._max_animali} Disponibile"
