#!/usr/bin/env python

import sys
import os
import requests  # if using Python2
#from urllib.request import urlopen

def check_args(argc, argv):

	if argc != 2:
		sys.stderr.write("Usage: "+__file__+" <url>\n")
		exit(1)
	
	if "http" not in sys.argv[1]:
		sys.stderr.write("<url> must be in form \"http://www.domain.com\"\n")
		exit(1)

	# for using Python2
	data = requests.get(sys.argv[1])
	return data.text

	# for using Python3 (am currently having trouble with https access w/ssl)
	#with urlopen(sys.argv[1]) as data:
		#return data.read().decode('utf-8', errors='ignore')

def print_list(paths):

	for i in paths:
		print(i)
		l = i.split('/')
		for d in l:
			sys.stdout.write(d+" >> ")
		sys.stdout.write('\n')

def make_dirs(file_path_unicode):
	file_path = list()	
	curr_dir = str
	curr_path = str

	file_path = file_path_unicode.encode('ascii', 'ignore').split('/')
	file_path.pop(0)
	curr_path = "."

	print(file_path_unicode+" "+str(len(file_path)))
	for curr_dir in file_path:
		curr_path += "/"+curr_dir
		sys.stdout.write(" >"+curr_path)
	sys.stdout.write('\n')	

def print_urls(home_html):
	file_path = str
	anchor = str
	start = int
	end = int

	anchor = "advancedfilmfl.com"
	start = 0

	while home_html[start:].find(anchor) != -1:
		start = home_html[start:].find(anchor) + start

		# if url is encapsulated by blank spaces, apostrophes or quotation marks
		end = min(
			home_html[start:].find(' '),
			home_html[start:].find('"'),
			home_html[start:].find("'"))

		file_path = home_html[start+len(anchor) : start+end]

		make_dirs(file_path)

		# to print entire url
		#print("https://www."+home_html[start:start+end])	

		start = start+end

def main(argc, argv):
	home_html = str

	home_html = check_args(argc, argv)

	print_urls(home_html)

	p = "./thi"
	if os.path.exists(p) == False:
		os.mkdir(p, 0775)	
		print(__file__+": \""+p+"\" created")
	else:
		print(__file__+": \""+p+"\" exists")

main(len(sys.argv), sys.argv)
