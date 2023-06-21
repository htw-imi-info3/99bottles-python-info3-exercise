class Song():
    def verse(self, n):

        result = \
            f"{n} bottles of mate on the wall, " + \
            f"{n} bottles of mate.\n" + \
            "Take one down and pass it around, " + \
            f"{n-1} bottles of mate on the wall.\n"

        return result

    def song(self):
        verses = [self.verse(n) for n in range(99, -1, -1)]
        return "\n".join(verses)
