import pytest  # noqa: F401
from config import xfail_new_feature_crates # noqa: F401, E261
from song import Song
from test.lyrics.whole_song_crates import song_lyrics, verses  # noqa: F401, E261


@pytest.mark.xfail(True, reason="new feature crate")
def test_4_crates():
    assert Song().verse(80) == verses[80]


@pytest.mark.xfail(True, reason="new feature crate")
def test_1_crate():
    assert Song().verse(20) == verses[20]


test_verses = [81, 80, 61, 60, 41, 40, 21, 20, 0]

@pytest.mark.parametrize("verse_number", test_verses)
@pytest.mark.xfail(xfail_new_feature_crates, reason="new feature: crates")
def test_verse(verse_number):
    assert Song().verse(verse_number) == verses[verse_number]


@pytest.mark.xfail(True, reason="new feature crate")
def test_whole_song_crates():
    assert Song().song() == song_lyrics
