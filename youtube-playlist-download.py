import os
from pytube import YouTube
from pytube import Playlist
#url = "https://www.youtube.com/playlist?list=PLZ6JdHLuUi0IO2GE7xMR-uf4xlxZqA8OG"
url = input("Enter you Url: \n")
links = ["https://www.youtube.com/" + i for i in Playlist(url).parse_links()]
print('\ntotal videos for download: ', len(links))

def download():
	for num, link in enumerate(links):
	    try:
	    	a = os.listdir()
	    	if not YouTube(link).streams.filter(subtype='mp4').all()[0].default_filename in a:
		    	YouTube(link).streams.filter(subtype='mp4').all()[0].download()
		    	print(num+1, '----- Links completed')
		    	links.remove(link)
	    	else:
	    		print(num+1, '----- Already downloaded')
	    except: pass

if not links:
	print('Download completed....!')
	os.system('nautilus ./')
else:
	print("---------------------------------------------------")
	for i in links:
		print(i)
	print("---------------------------------------------------")
	download()
