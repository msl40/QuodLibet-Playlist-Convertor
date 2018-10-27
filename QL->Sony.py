
__author__ = "Michael Liu"
__version__ = "1.0"
__email__ = "mikeliu.2000@gmail.com"
__status__ = "testing"

import os
import sys
import urllib2

playlistDict = {}


def open_files(pathToFile):
	'''
		pathToFile = command line input argument, file path to QuodLibet playlists
		
		this method opens all 
	'''
	for filename in os.listdir(pathToFile):
		if filename == ".DS_Store":
			# ignore the .DS_Store file
			continue
		else:
			# print("converting playlist: " + filename)
			playlist = []
			fullPath = pathToFile + "/" + filename
			file = open(fullPath,"r")
			songList = file.readlines()
			while len(songList) > 0:
				song = songList[0]
				playlist.append(song)
				songList.pop(0)
			playlistDict[filename] = playlist
			file.close()



def convert():
	'''
		in a QuodLibet playlist file, a song's path may be: 
			/Users/username/path/Blurryface (Album)/05 Tear In My Heart.flac
		for sucessful conversion, must delete everything before album name
		ending string will be:
			Blurryface (Album)/05 Tear In My Heart.flac
	'''
	deleteString = "/Users/mikeliu/Music/"
	# deleteString = path to your music folder
	
	for playlist, songs in playlistDict.items():
		
		cleaned_songs = []
		
		for each in songs:
			each = each.strip("\n")
			each = each.replace(deleteString, "")	
			cleaned_songs.append(each)

		playlistDict[playlist] = cleaned_songs
	
	return




def create_files():
	save_path = "/Users/mikeliu/Music"
	os.path.join(save_path, )
	for playlist, songs in playlistDict.items():

		clean_playlist = urllib2.unquote(playlist)
		# print clean_playlist

		file_out = open(save_path + "/" + clean_playlist + ".M3U8", "w")
		file_out.write("#EXTM3U\n")
		for each in songs:
			file_out.write("#EXTINF:,\n")
			file_out.write(each + "\n")
		file_out.close()
	return


def printdict():
	print ("Dictionary: ")
	for playlist, songs in playlistDict.items():
		print playlist
		for each in songs:
			print each



if __name__ == "__main__":
		
	# print (str(sys.argv))
	
	filePath = sys.argv[1]

	open_files(filePath)
	# printdict()

	convert()
	# printdict()

	create_files()


