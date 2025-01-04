import json

def cmp_items(item: tuple):
    k, v = item
    return v

with open("StreamingHistory.json", "r", encoding = "utf8") as file:
    history = json.load(file)

artists = {}
tracks = {}

for play in history:
    artist = play['artistName']

    if artist not in artists:
        artists[artist] = 1
    else:
        artists[artist] += 1
    
    track = play['trackName']

    if track not in tracks:
        tracks[track] = 1
    else:
        tracks[track] += 1

artists_streams = list(artists.items())
artists_streams.sort(key = cmp_items, reverse = True)

print('Top 10 artists:')
for i in range(10):
    a, n = artists_streams[i]
    print(f'\t{i + 1:2} - {a} : {n} streams')

tracks_streams = list(tracks.items())
tracks_streams.sort(key = cmp_items, reverse = True)

print('Top 10 tracks:')
for i in range(10):
    t, n = tracks_streams[i]
    print(f'\t{i + 1:2} - {t} : {n} streams')