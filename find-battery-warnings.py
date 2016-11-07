#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Mikko K <mki@iki.fi>, 2016 
#
import re
import sys
from os import listdir
from os.path import isdir, isfile, join

#
DEFAULT_LOGS_DIR="C:\EResultsLite\logfiles"

if len(sys.argv) > 1:
	mypath = sys.argv[1]
else:
	mypath = DEFAULT_LOGS_DIR
	
if not isdir(mypath):
	#
	print "Lokihakemistoa %s ei ole tai se on annettu väärä." % mypath
	sys.exit(2) 

logfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for filename in logfiles:
	#
	# Filter files
	if filename.startswith("250"):
		file = open(filename, "r")
		varoitukset = {}
		varoitukset_emit = {}
		for line in file:
			#
			# Find battery warnings
			if re.search("099", line):
				items = line.split(",")
				for idx, item in enumerate(items):
					if item == "099":
						leimasin = items[idx-2]
						#
						# Emit card warning
						if leimasin == "250":
							emitnro = items[3]
							if emitnro in varoitukset_emit:
								varoitukset_emit[emitnro] = varoitukset_emit[emitnro]+1
							else:
								varoitukset_emit[emitnro] = 1
						else:
							#
							# Emit post warning
							if leimasin in varoitukset:
								varoitukset[leimasin] = varoitukset[leimasin]+1
							else:
								varoitukset[leimasin] = 1
		if len(varoitukset) > 0 or len(varoitukset_emit) > 0:
			#
			# Print file name for timestamp observations
			print "\n" + filename
		if len(varoitukset) > 0:
			#
			# print "\tBattery warnings from posts:"
			print "\tParisto varoitukset rastileimasimista:"
			for leimasin in varoitukset:
				print "\t" + leimasin + ": " + str(varoitukset[leimasin])
		if len(varoitukset_emit) > 0:
			#
			# print "\tBattery warnings from cards:"
			print "\tParisto varoitukset emit-korteista:"
			for leimasin in varoitukset_emit:
				print "\t" + leimasin + ": " + str(varoitukset_emit[leimasin])