from pytube import Playlist
from pytube import YouTube
url = 'https://www.youtube.com/watch?v=30KcXAgiUDA&list=PLRo0dT6sKvOZJe-soWVJ-c1_QtDzpz_d0'

plist = Playlist( url )

for i in plist:
    yt = YouTube(i)
    yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').last().download('./yt')