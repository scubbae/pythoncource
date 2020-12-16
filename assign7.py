# My favorite song by Mariaha Carry

myFavoriteSong = {
    'Artist': 'Maria Cary',
    'Title': 'Butterfly',
    'Album': 'Butterfly',
    'Date': '1997',
    'Genre': 'Contemporary R&B'
}

for key, val in myFavoriteSong.items():
    print(key, ':', val)

print("\n")


def guess():
    song = list(myFavoriteSong.values())
    if input("what is my favorite song or artist?:").capitalize() in song:
        print("success")
    else:
        print("Nope! try again")


guess()
