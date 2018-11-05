#!/usr/local/bin/python3
# GuGuRenamer
# coding="utf-8"

# ----------------------------------------------------------------------------------
# How to use this Script
# 0) Install Python3 in package Center
# 1) Place this GuGURenamer folder inside the Anime Directory
# 2) if you want to only rename file in one specific folder, please copy the absolute path to below:
# 2) Otherwise, this script will scan all folders next to GuGuRenamer folder
# eg. specificpath = "/volume1/Multimedia/Animation/Sword Art Online"
path = ""
# 3)spcific filetype for files needed to be renamed
types = ('*.mkv', '*.mp4') 
# 4) Check the full path to the GuGuRenamer.py eg. "/volume1/Multimedia/Animation/GuGuRenamer/GuGuRenamer.py"
# 5) Run this script, enter the below cmd in ssh,
#	ie. .<full path to GuGURenamer.py>
#	eg. ./volume1/Anime/Anime/GuGuRenamer/GuGuRenamer.py
# ----------------------------------------------------------------------------------

import glob, re, os, csv, sys

#define path to scan
if not path:
	path = os.path.dirname(os.path.abspath(__file__))+"/../**/"
else:
	path = path + "/**/"	
print("Scanning: " + path) #for debug use

#serach files with specified filetype
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob( path + files))
    files_grabbed.extend(glob.glob( path + "**/" + files))
files_grabbed   # the list of pdf and cpp files
#print(files_grabbed) #for debug use
#sys.exit("Stop for Debug")

# define dictionay as dictionary
dictionary = {}

#open the Dictionary.csv file with using utf-8 coding
reader = csv.reader(open( os.path.dirname(os.path.abspath(__file__))+'/Dictionary.csv', 'r', encoding="utf-8"))
#print("Dict: " + os.path.dirname(os.path.abspath(__file__))+'/Dictionary.csv') #for debug use

#put result of csv.reader to the Dictionary
for dmhyname, plexname in reader:
   dictionary[dmhyname] = plexname

#start rename process
for filename in files_grabbed:
   #duplicate filename to new_name
   new_name = filename
   #print(new_name + "\n") #for debug use
   #search if new_name contain sting in dictionary
   for key in dictionary:  
      #print("Dict(Find)") #for debug use
      #print(key) #for debug use
      #print("Dict(Repl)") #for debug use
      #print(dictionary[key]) #for debug use
      
      #prepare the new_name for renaming
      new_name = new_name.replace(key, dictionary[key])
   #rename the file
   os.rename(filename, new_name)
   
   #print result if renamer has renamed any file
   if (filename != new_name):
      print("Renamed: \n" + filename + "\n to: \n" + new_name + "\n")
      
sys.exit("End: GuGuRenamer Execution Completed")