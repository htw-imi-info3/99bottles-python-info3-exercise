from song.song import Song as SongV1          # noqa: F401, E261
# from song.song_solution import Song as SongV2  # noqa: F401, E261


# Implementation: This can be used to switch to an alternate version in
# song/__init__.py

Song = SongV1

# Test Behaviour
skip_not_implemented = False
xfail_changing = True
xfail_new_feature_crates = True
