import pytest  # noqa: F401
from config import Song, xfail_changing, skip_not_implemented
from test.lyrics.whole_song import song_lyrics


def test_85():
    verse = """\
85 bottles of mate on the wall, 85 bottles of mate.
Take one down and pass it around, 84 bottles of mate on the wall.
"""
    assert Song().verse(85) == verse


@pytest.mark.skipif(False, reason="not yet implemented")
def test_86():
    verse = """\
86 bottles of mate on the wall, 86 bottles of mate.
Take one down and pass it around, 85 bottles of mate on the wall.
"""
    assert Song().verse(86) == verse


@pytest.mark.skipif(skip_not_implemented, reason="not yet implemented")
def test_3():
    verse = """\
3 bottles of mate on the wall, 3 bottles of mate.
Take one down and pass it around, 2 bottles of mate on the wall.
"""
    assert Song().verse(3) == verse


@pytest.mark.skipif(skip_not_implemented, reason="not yet implemented")
def test_2():
    verse = """\
2 bottles of mate on the wall, 2 bottles of mate.
Take one down and pass it around, 1 bottle of mate on the wall.
"""
    assert Song().verse(2) == verse


@pytest.mark.skipif(skip_not_implemented, reason="not yet implemented")
def test_1():
    verse = """\
1 bottle of mate on the wall, 1 bottle of mate.
Take it down and pass it around, no more bottles of mate on the wall.
"""
    assert Song().verse(1) == verse


@pytest.mark.skipif(skip_not_implemented, reason="not yet implemented")
def test_0():
    verse = """\
No more bottles of mate on the wall, no more bottles of mate.
Go to the store and buy some more, 99 bottles of mate on the wall.
"""
    assert Song().verse(0) == verse


@pytest.mark.skipif(skip_not_implemented, reason="not yet implemented")
@pytest.mark.xfail(xfail_changing, reason="this breaks with crates implemented")
def test_whole_song():
    assert Song().song() == song_lyrics
