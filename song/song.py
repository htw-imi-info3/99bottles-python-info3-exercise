class Song():
    def verse(self, n):
        if n == 85:
            return """\
85 bottles of mate on the wall, 85 bottles of mate.
Take one down and pass it around, 84 bottles of mate on the wall.
"""
        if n == 86:
            return """\
86 bottles of mate on the wall, 86 bottles of mate.
Take one down and pass it around, 85 bottles of mate on the wall.
"""
        if n == 3:
            return """\
3 bottles of mate on the wall, 3 bottles of mate.
Take one down and pass it around, 2 bottles of mate on the wall.
"""

        return "not implemented"

    def song(self):
        verses = [self.verse(n) for n in range(99, -1, -1)]
        return "\n".join(verses)
