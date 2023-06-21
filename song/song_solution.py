# from song.whole_song import song_lyrics

do_crates = True


class BottleNumber:

    def __init__(self, n):
        self.n = n

    def successor(self):
        return BottleNumberFactory.for_n(self.n - 1)

    def __str__(self):
        return f"{self._quantity()} {self._container()}"

    def _quantity(self) -> str:
        return self.n

    def _container(self):
        return "bottles"

    def action(self):
        return f"Take {self._pronoun()} {self._preposition()} " +\
            "and pass it around"

    def _pronoun(self):
        return "one"

    def _preposition(self):
        return "down"


class OneBottle(BottleNumber):

    def _pronoun(self):
        return "it"

    def _container(self):
        return "bottle"


class NoBottles(BottleNumber):

    def _quantity(self):
        return "no more"

    def action(self):
        return "Go to the store and buy some more"

    def successor(self):
        return BottleNumberFactory.for_n(99)


class Crates(BottleNumber):
    size = 20

    def _quantity(self):
        return str(int(self.n/self.size))

    def _container(self):
        return "crates"

    def _preposition(self):
        return "out"


class OneCrate(Crates):
    def _container(self):
        return "crate"


class BottleNumberFactory:
    bottle_map = [
        [lambda n: n == 0, NoBottles],
        [lambda n: n == 1, OneBottle],
        [lambda n: n == 20, OneCrate],
        [lambda n: n % Crates.size == 0, Crates]
    ]
    
    @classmethod
    def for_n(cls, n):
        for predicate, bottles_class in cls.bottle_map:
            if predicate(n):
                return bottles_class(n)

        return BottleNumber(n)

class Song:

    def song(self):
        verses = [self.verse(n) for n in range(99, -1, -1)]
        return "\n".join(verses)

    def verse(self, n):
        bn = BottleNumberFactory.for_n(n)
        result = f"{str(bn).capitalize()} of mate on the wall, " + \
                 f"{bn} of mate.\n" + \
                 f"{bn.action()}, {bn.successor()} of mate on the wall.\n"
        return result
