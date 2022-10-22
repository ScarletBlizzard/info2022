from random import choice


class RNA:
    NUCLEOTIDES = ["A", "U", "G", "C"]
    COMPLEMENTS = {
        "A": "T",
        "U": "A",
        "G": "C",
        "C": "G"
    }

    def __init__(self, chain=""):
        for n in chain:
            if n not in self.NUCLEOTIDES:
                raise ValueError((f"{type(self).__name__} chain must contain only "
                    f"{', '.join(self.NUCLEOTIDES)}"))
        self._chain = chain

    @classmethod
    def from_list(cls, lst):
        return cls("".join(lst))

    @classmethod
    def from_str(cls, str):
        return cls(str)

    @classmethod
    def nucleotide_complement(cls, nucleotide):
        return cls.COMPLEMENTS[nucleotide]

    def complementary_DNA(self):
        return DNA.from_list([self.nucleotide_complement(n) for n in self._chain])

    def __getitem__(self, idx):
        return self._chain[idx]

    def __add__(self, other):
        return self.from_str(self._chain + other._chain)

    def __repr__(self):
        return f"{type(self).__name__}({self._chain})"

    def __str__(self):
        return self._chain

    def get_chain(self):
        return str(self)

    def __mul__(self, other):
        new_chain = []
        for pair in zip(self._chain, other._chain):
            new_chain.append(choice(pair))

        min_len = len(other._chain)
        longer_chain = self._chain
        if len(self._chain) < len(other._chain):
            min_len = len(self._chain)
            longer_chain = other._chain
        new_chain.extend(longer_chain[min_len:])

        return self.from_list(new_chain)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self._chain == other._chain

    def __hash__(self):
        return hash(self._chain)


class DNA(RNA):
    NUCLEOTIDES = ["A", "T", "G", "C"]
    COMPLEMENTS = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    def __getitem__(self, idx):
        n = super().__getitem__(idx)
        return n, self.nucleotide_complement(n)

    def get_first_chain(self):
        return self.get_chain()

    def get_second_chain(self):
        return str(self.complementary_DNA())
