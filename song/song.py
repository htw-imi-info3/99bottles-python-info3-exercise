class Song():
    def verse(self, n):
        if n == 85:
            return """\
85 bottles of mate on the wall, 85 bottles of mate.
Take one down and pass it around, 84 bottles of mate on the wall.
"""

        return "not implemented"

    def song(self):
        verses = [self.verse(n) for n in range(99, -1, -1)]
        return "\n".join(verses)
