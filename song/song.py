class Song():
    def verse(self, n):
        if n == 2:
            return """\
2 bottles of mate on the wall, 2 bottles of mate.
Take one down and pass it around, 1 bottle of mate on the wall.
"""
        if n == 1:
            return """\
1 bottle of mate on the wall, 1 bottle of mate.
Take it down and pass it around, no more bottles of mate on the wall.
"""

        if n == 0:
            return """\
No more bottles of mate on the wall, no more bottles of mate.
Go to the store and buy some more, 99 bottles of mate on the wall.
"""

        result = \
            f"{n} bottles of mate on the wall, " + \
            f"{n} bottles of mate.\n" + \
            "Take one down and pass it around, " + \
            f"{n-1} bottles of mate on the wall.\n"

        return result

    def song(self):
        verses = [self.verse(n) for n in range(99, -1, -1)]
        return "\n".join(verses)
