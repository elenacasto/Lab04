from CabinaStandard import CabinaStandard

class CabinaAnimali(CabinaStandard):
    def __init__(self, codice, num_letti, ponte, prezzo, max_animali):
        super().__init__(codice, num_letti, ponte, prezzo)
        self._max_animali = int(max_animali)

    @property
    def prezzo(self):
        return self._prezzo * (1 + 0.10 * self._max_animali)

    def __str__(self):
        stato = "Disponibile" if self._disponibile else "Occupata"
        return (f"{self._codice} : Animali | {self._num_letti} letti - Ponte {self._ponte} - "
                f"Prezzo - {self.prezzo} - Max animali: {self._max_animali} {stato}")
