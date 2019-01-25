import os
from pytube import YouTube
from pytube import Playlist
url = "https://www.youtube.com/playlist?list=PLZ6JdHLuUi0IO2GE7xMR-uf4xlxZqA8OG"
links = ["https://www.youtube.com/" + i for i in Playlist(url).parse_links()]
print('\ntotal videos for download: ', len(links))

def download()
	for num, link in enumerate(links):
	    try:
	    	YouTube(link).streams.filter(subtype='mp4').all()[0].download()
	    	print(num+1, '----- Links completed')
	    	links.remove(link)
	    except: pass

if not links:
	print('Download completed....!')
	os.system('nautilus ./')
else:
	download()