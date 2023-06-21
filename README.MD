## 99 Bottles of Mate Exercise

### Assignment: 

- Implement the verse(n) method in Song [(song/song.py)](song/song.py)
  which should return the respective single verse from the [whole song](test/lyrics/whole_song.py). 
- If all verses are returned correctly, Song#song() returns the whole Song.
- Tests are already there. 
- You can use [config.py](config.py) to switch off test skipping/xfailing.

Change:
- Crates with 20 bottles each should be handled differently, as in [test/lyrics/whole_song_crates.py](test/lyrics/whole_song_crates.py)

### How to Refactor: 

If you have no Idea how to refactor best, simply find the worst code smell and get rid of it:
- [Wikipedia on Code Smells](https://en.wikipedia.org/wiki/Code_smell)
- [Refactoring Guru: Code Smells](https://refactoring.guru/refactoring/smells)
- [Catalog of Refactorings](https://refactoring.com/catalog/)

## This exercise is inspired by the 
- [99 bottles of beer kata](https://www.codewars.com/kata/99-bottles-of-beer-1/javascript)
- Sandi Metz' Book [99 Bottles of OOP - 2nd Edition](https://sandimetz.com/99bottles)