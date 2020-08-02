from listsTuples03.nested_data130 import albums

# creating constants
SONG_INDEX = 1
SONGS_LIST_INDEX = 3

while True:
    print("Please choose your album (invalid choice exists):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]

        for index, songs in enumerate(songs_list):
            print("{}: {}".format(index + 1, songs[SONG_INDEX]))

        song_choice = int(input())
        if 1 <= song_choice <= len(songs_list):
            print("Playing {}".format(songs_list[song_choice - 1][SONG_INDEX]))
            print("=" * 40)
        else:
            continue
    else:
        continue
