#!/usr/bin/env python
#coding: utf8 

import dircache
import os
import re

#-------------------------------------------------------------------------------

# Arbeitsverzeichnis
workdir = './'

# Ausgangsmaterial, nach dem gesucht werden soll
srctype = 'wma'

#-------------------------------------------------------------------------------

# Dateilisten
filesInWorkdir = dircache.listdir(workdir)

for file in filesInWorkdir:

	# nur WMA-Dateien bearbeiten
	if str(file).split('.')[-1] == srctype:
		
		# Neuen Dateinamen aus dem Alten bilden
		newFileName = str(file).split('.' + srctype)[0] + '.mp3'
		
		# Mit ffmpeg umwandeln	
		os.popen("ffmpeg -i " + re.escape(workdir + "/" + file) + " -codec:a libmp3lame -qscale:a 2 " + re.escape(workdir + "/" + newFileName) + " 1&> /dev/null")
			
		print file + " umgewandelt -> " + newFileName
			
#-------------------------------------------------------------------------------

# Terminal-Befehl für ffmpeg:
# DS> ffmpeg -i input.wma -codec:a libmp3lame -qscale:a 2 output.mp3

# Average kbit/s | Bitrate range kbit/s | ffmpeg option
# ---------------+----------------------+-------------------------------------------
# 320            | 320 CBR (non VBR)    | -b:a 320k (NB this is 32KB/s, or its max)
# 245            | 220-260              | -q:a 0 (NB this is VBR from 22 to 26 KB/s)
# 225            | 190-250              | -q:a 1
# 190            | 170-210              | -q:a 2
# 175            | 150-195              | -q:a 3
# 165            | 140-185              | -q:a 4
# 130            | 120-150              | -q:a 5
# 115            | 100-130              | -q:a 6
# 100            | 80-120               | -q:a 7
# 85             | 70-105               | -q:a 8
# 65             | 45-85                | -q:a 9
