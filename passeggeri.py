class Passeggeri:
    def __init__(self, codice_passeggero, nome_passeggero, cognome):
        self._codice_passeggero = codice_passeggero
        self._nome_passeggero = nome_passeggero
        self._cognome = cognome
        self._cabina = None

    def __str__(self):
        cabina = self._cabina.codice if self._cabina else "Nessuna cabina assegnata"
        return f"{self._codice_passeggero}: {self._nome_passeggero} {self._cognome} - Cabina: {cabina}"