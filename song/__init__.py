from config import use_alternate_song_implementation
from song.song import Song as SongV1          # noqa: F401, E261
from song.song_solution import Song as SongV2  # noqa: F401, E261

if use_alternate_song_implementation:
    Song = SongV2
else:
    Song = SongV1
