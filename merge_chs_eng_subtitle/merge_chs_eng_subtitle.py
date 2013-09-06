#! /usr/bin/env python

import time
import sys
import exceptions
import string


def main(argv=sys.argv):
	englist_title_file = open(argv[1],"r")
	chinese_title_file = open(argv[2],"r")
	mixed_title_file = open(argv[3],"w")
	sub_index = 1
	sub_content = {}
	while 1 :
		### index line
		line = englist_title_file.readline()

		if not line or line=="" or line=="\r" or line=="\r\n":
			break

		if sub_index == string.atoi(line):
			### sub time line
			englist_title_file.readline()
			### english subtitle line
			sub_content[sub_index] = englist_title_file.readline()
			### blank line
			englist_title_file.readline()

			sub_index += 1	
	sub_index_max = sub_index		

	print "sub_max:", sub_index_max

	sub_index = 1	
	while 1 :
		### index line
		line = chinese_title_file.readline()
		mixed_title_file.write(line)

		print "xxxxx=    "+line
		if not line or line=="" or line=="\r" or line=="\r\n":
			break

		if sub_index == string.atoi(line):
			### sub time line
			line = chinese_title_file.readline()
			mixed_title_file.write(line)
			### chinese subtitle line
			line = chinese_title_file.readline()
			mixed_title_file.write(line)
			### english subtitle line
			line = sub_content[sub_index]
			mixed_title_file.write(line)
			### blank line
			line = chinese_title_file.readline()
			mixed_title_file.write(line)

			sub_index += 1
		if sub_index >= sub_index_max :
			break

	englist_title_file.close()
	chinese_title_file.close()
	mixed_title_file.close()



if __name__ == "__main__":
	sys.exit(main())




	
