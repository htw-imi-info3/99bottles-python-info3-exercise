# from song.whole_song import song_lyrics

do_crates = True


class BottleNumber:

    @staticmethod
    def class_for(n):
        return True

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


class NoBottles(BottleNumber):

    @staticmethod
    def class_for(n):
        return n == 0

    def _quantity(self):
        return "no more"

    def action(self):
        return "Go to the store and buy some more"

    def successor(self):
        return BottleNumberFactory.for_n(99)


class OneBottle(BottleNumber):

    @staticmethod
    def class_for(n):
        return n == 1

    def _pronoun(self):
        return "it"

    def _container(self):
        return "bottle"


class Crates(BottleNumber):
    size = 20

    @classmethod
    def class_for(cls, n):
        return n > cls.size and n % cls.size == 0

    def _quantity(self):
        return str(int(self.n/self.size))

    def _container(self):
        return "crates"

    def _preposition(self):
        return "out"


class OneCrate(Crates):
    @classmethod
    def class_for(cls, n):
        return n == cls.size

    def _container(self):
        return "crate"


class BottleNumberFactory:

    classes = []

    @classmethod
    def register(cls, bottle_number_class):
        cls.classes.insert(0, bottle_number_class)

    @classmethod
    def for_n(cls, n):
        for bottle_number_class in cls.classes:
            if bottle_number_class.class_for(n):
                return bottle_number_class(n)


BottleNumberFactory.register(BottleNumber)
BottleNumberFactory.register(NoBottles)
BottleNumberFactory.register(OneBottle)

if do_crates:
    BottleNumberFactory.register(Crates)
    BottleNumberFactory.register(OneCrate)


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
