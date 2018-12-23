# Convert Quod Libet Playlist file to M3U8

Python script to convert [Quod Libet](https://quodlibet.readthedocs.io/en/latest/#) playlist file to M3U8 playlist file compatible with Sony ZX and Sony NW series audio players.

## Getting Started

Download and install [Python 3](https://www.python.org/downloads/)

## Running the Script

Download QL->Sony.py script, open Terminal and navigate to folder containing script  
i.e.:  
	cd /Users/username/Downloads


Run the script with correct inputs in Terminal  
i.e.:  
	python3 ./QL-\>Sony.py /Users/username/.quodlibet/playlists /Users/username/MusicFolder /Users/username/PathToWriteTo


This python script takes three inputs:

* **Input 1** = path to Quod Libet playlist folder, should be in the form:  
	/Users/username/.quodlibet/playlists  
	- See [Quod Libet FAQs](https://quodlibet.readthedocs.io/en/latest/guide/faq.html)
* **Input 2** = path to source folder containing all Quod Libet music
	- To find the correct file path: 
		- Open up a Quod Libet playlist file in any text editor
		- Inside a Quod Libet playlist file, you'll see:
	
			/Users/username/Music/More Life (Album)/08 4422.flac  
			/Users/username/Music/Beauty Behind The Madness (Album)/06 Acquainted.flac  
			/Users/username/Music/Kaleidoscope Dream The Water Preview (Single)/01 Adorn.flac  
			/Users/username/Music/So Far Gone (Album)/03 Best I Ever Had.flac  
			/Users/username/Music/California (Single)/01 California.flac  

		- The correct file path to input into the script for the above example would be: /Users/username/Music/
			- You want the lowest level folder that still contains all the music files
			- Make sure you include the last backslash!
* **Input 3** = path to write new playlist files to
	- This can be any folder location of your choosing
	- In this example I'll choose the same folder as where the music is stored: /Users/username/Music
* **What command line should look like using above example:** = path to write new playlist files to
	python3 ./QL-\>Sony.py  /Users/username/.quodlibet/playlists  /Users/username/Music  /Users/username/PathToWriteTo


## Built With

* [Quod Libet](https://quodlibet.readthedocs.io/en/latest/#) - GTK+ - based audio player written in Python
* [Sublime Text](https://www.sublimetext.com/) - Text editor


## Authors

* **Michael Liu** - [msl40](https://github.com/msl40)

