import pytest  # noqa: F401
from test.lyrics.whole_song_crates import song_lyrics, verses  # noqa: F401, E261
from config import xfail_changing, skip_not_implemented  # noqa: F401, E261


def test_verses_len():
    assert len(verses) == 100


def test_verse_80_split():
    assert verses[80] == '4 crates of mate on the wall, 4 crates of mate.\n' +\
        'Take one out and pass it around, 79 bottles of mate on the wall.\n'


def test_verse_0_split():
    assert verses[0] == 'No more bottles of mate on the wall, ' + \
        'no more bottles of mate.\n' +\
        'Go to the store and buy some more, 99 bottles of mate on the wall.\n'
