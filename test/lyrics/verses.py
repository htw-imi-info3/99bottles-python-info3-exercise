
def split_verses(song_lyrics):
    verses = song_lyrics.split('\n\n')
    verses = [v.strip() for v in verses]
    verses = [f"{v}\n" for v in verses]
    verses.reverse()
    return verses
