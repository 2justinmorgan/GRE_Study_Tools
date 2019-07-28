#!/usr/bin/env python3

import sys

def check_book_format(book_file):
	anchor = str
	line_num = int

	line_num = 1

	for line in book_file:
		if "MANHATTAN PREP" not in line and line_num == 1:
			return 1
		if "5* lb. Book of GRE" not in line and line_num == 2:
			return 1	

		line_num += 1

		if line_num > 2:
			break

	return 0

def check_args():
	
	if len(sys.argv) != 2:
		sys.stderr.write("Usage: "+__file__+" <book.txt>\n")
		exit(1)
	
	book_file = open(sys.argv[1], "r")

	if check_book_format(book_file) != 0:
		sys.stderr.write('\n')
		sys.stderr.write(__file__+": \""+sys.argv[1]+"\" is not in the correct"+
			" .txt format of\nManhattan's .pdf version of the 5lb GRE Prep Book"+
			". To get the book\nin the correct .txt format, execute the command"+
			":\n\n  # pdftotext -layout <Manhattan_5lb_Book.pdf> "+
			"<Manhattan_5lb_Book.txt>\n")
		sys.stderr.write('\n')
		exit(1)

	return book_file.read()

def get_catagory(catagory_num, table_of_contents):
	curr_line = str
	start = int
	end = int

	start = table_of_contents.index(str(catagory_num) + ". ")
	curr_line = table_of_contents[start:]
	end = curr_line.index('\n')
	
	return curr_line[len(str(catagory_num)) + 2 :end]

def get_table_of_contents_page(book_text):
	anchor = str
	start = int

	anchor = "TABLE of CONTENTS"
	start = book_text.index(anchor) + len(anchor)

	return book_text[start:]

def get_num_of_questions(catagory, book_text):
	anchor = str
	num = int
	start = int
	end = int

	anchor = catagory + " Answers" 
	num = 1
	start = book_text.index(anchor) + len(anchor)
	end = book_text[start:].index(anchor)

	while str(num) + "." in book_text[start:start+end]:
		num += 1

	return num-1

def get_table_of_contents(book_text):
	table_of_contents = list()
	catagories_range = list()
	catagory_num = int
	table_of_contents_page = str
	catagory = str

	catagories_range = range(7, 30)
	table_of_contents_page = get_table_of_contents_page(book_text)

	for catagory_num in catagories_range:
		catagory = get_catagory(catagory_num, table_of_contents_page)
		table_of_contents.append(catagory)
		table_of_contents.append(get_num_of_questions(catagory, book_text))
		
	return table_of_contents

def print_questions_breakdown(table_of_contents):
	index = int

	for index in range(0, len(table_of_contents), 2):
		sys.stdout.write(str(int(index/2)+1)+") ")
		print(str(table_of_contents[index+1])+" in "+table_of_contents[index])

def main():

	table_of_contents = list()

	book_text = check_args() 

	table_of_contents = get_table_of_contents(book_text)

	print_questions_breakdown(table_of_contents)

main()
