import os
from pytube import YouTube
from pytube import Playlist
url = input("Enter you playlist Url: \n")
try:
	len(url)
	links = ["https://www.youtube.com/" + i for i in Playlist(url).parse_links()]
except:
	links = open('links.txt', 'r').read().splitlines()

l = len(links)
print('\ntotal videos for download: ', len(links))

def download():
	for num, link in enumerate(links[::-1]):
	    try:
	    	a = os.listdir()
	    	b = YouTube(link).streams.filter(subtype='mp4').all()[0]
	    	if not b.default_filename in a:
	    		b.download() 
		    	print(num+1, '----- Links completed')
		    	links.remove(link)
	    	else:
	    		print(num+1, '----- Already downloaded')
	    except: pass


while links:
	print("----------------Download list----------------")
	for i in links:
		print(i)
	print("---------------------------------------------------")
	download()


print('Download completed....!')
os.system('nautilus ./')	
