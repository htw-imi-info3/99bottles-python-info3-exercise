import pytest  # noqa: F401
from config import Song, xfail_changing, skip_not_implemented  # noqa: F401, E261
from test.lyrics.whole_song import song_lyrics, verses  # noqa: F401, E261


test_original_verses = [86, 85, 15, 2, 1, 0]

@pytest.mark.parametrize("verse_number", test_original_verses)
@pytest.mark.xfail(skip_not_implemented, reason="original behaviour")
def test_verse(verse_number):
    assert Song().verse(verse_number) == verses[verse_number]


@pytest.mark.xfail(xfail_changing, reason="this test will not work once crates are added")
def test_whole_song():
    assert Song().song() == song_lyrics
