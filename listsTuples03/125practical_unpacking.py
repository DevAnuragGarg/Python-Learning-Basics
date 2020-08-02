for t in enumerate("abcdefg"):
    print(t)

# this will print tuple
for t in enumerate("abcdefg"):
    index, character = t
    print(index, character)

imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1984
title, artist, year = imelda
print(title)
print(artist)
print(year)

table = ("Coffe table", 20, 100, 49.5)
print(table[1] * table[2])

# nested tuples
albums = [("More Mayhem", "Emilda May", 2011),
          ("Ride the lightning", "Metallica", 1984),
          ("Ride the lightning", "Metallica", 1984),
          ("Ride the lightning", "Metallica", 1984)]

for title, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(title, artist, year))

# you can't append to tuple because tuples are immutable.
