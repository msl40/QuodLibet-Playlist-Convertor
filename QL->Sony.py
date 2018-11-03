
__author__ = "Michael Liu"
__version__ = "1.0"
__email__ = "mikeliu.2000@gmail.com"
__status__ = "completed"

import os
import sys
import urllib.request

playlistDict = {}



'''
	open all Quod Libet playlist files and read data into dictioanry
	pathToFile = command line input argument, file path to QuodLibet playlists
'''
def open_files(pathToFile):
	for filename in os.listdir(pathToFile):
		if filename == ".DS_Store":
			# ignore the .DS_Store file
			continue
		else:
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



'''
	convert format/syntax of playlist file to be compatible with Sony players
	in a QuodLibet playlist file, a song's path may be: 
		/Users/usrname/path/Blurryface (Album)/05 Tear In My Heart.flac
	
	for sucessful conversion, must delete everything before album name
	ending string will be:
		Blurryface (Album)/05 Tear In My Heart.flac
	
	deleteString = path to common music folder
'''
def convert(deleteString):
	for playlist, songs in playlistDict.items():	
		cleaned_songs = []
		for each in songs:
			each = each.strip("\n")
			each = each.replace(deleteString, "")	
			cleaned_songs.append(each)
		playlistDict[playlist] = cleaned_songs
	return



'''
	write the new, converted dictionary to new playlist files
	write one new M3U8 playlist file per key in dictionary, contents of playlist file are dictionary values
	writePath = file path to write new playlist files to 	
'''
def create_files(writePath):
	os.path.join(writePath, )
	for playlist, songs in playlistDict.items():
		clean_playlist = urllib.request.unquote(playlist)
		file_out = open(writePath + "/" + clean_playlist + ".M3U8", "w")
		file_out.write("#EXTM3U\n")
		for each in songs:
			file_out.write("#EXTINF:,\n")
			file_out.write(each + "\n")
		file_out.close()
	return


'''
	prints dictionary converted playlists
	key = playlist name
	value = songs in the playlist
'''
def printdict():
	print ("Dictionary: ")
	for playlist, songs in playlistDict.items():
		print (playlist)
		for each in songs:
			print (each)



'''	
	input 1 = file path to Quod Libet playlist folder 
	i.e. /Users/usrname/.quodlibet/playlists

	input 2 = file path to folder where all local Quod Libet music is stored
		for help finding this, open a Quod Libet playlist 
		it is the first part of very string normally beginning with
		i.e. /Users/usrname/Music/ or /Users/usrname/PathToMusic... 

	input 3 = file path to write new playlist files to
'''
if __name__ == "__main__":
	
	filePath = sys.argv[1]
	deleteString = sys.argv[2]
	writePath = sys.argv[3]
	
	# open Quod Libet playlist files and read in data to dictionary
	open_files(filePath)

	# convert format/syntax of playlist data to be compatibile with Sony players
	convert(deleteString)

	# write new playlist files to given path 
	create_files(writePath)


