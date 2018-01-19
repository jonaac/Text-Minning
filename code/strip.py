from bs4 import BeautifulSoup
import os
import re


def parse_and_create(path, path_to_write):
	for filename in os.listdir(path):
	    # do your stuff
	    if "http" in filename:
	    	sortedindex = open(path + filename, "r+")
	    	lines = sortedindex.readlines()
	    	aux = open('aux.html', "w+")
	    	start = 0
	    	for line in lines:
	    		if re.match('^[^\s*<]', line) is None or start != 0:
	    			aux.write(line)
	    			start = 1
	    	aux.close()
	    	fileUser = open(path_to_write + filename, "w+")
	    	soup = BeautifulSoup(open('aux.html'), "html.parser")
	    	txt = soup.get_text()
	    	fileUser.write(txt.encode('utf8'))
	    	os.remove('aux.html')

# Training set:

#course
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/course/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/course/strip/'

parse_and_create(path, path_to_write)

#faculty
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/faculty/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/faculty/strip/'

parse_and_create(path, path_to_write)

#student
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/student/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/student/strip/'

parse_and_create(path, path_to_write)

# Test set:
#course
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/course/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/course/strip/'

parse_and_create(path, path_to_write)

#faculty
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/faculty/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/faculty/strip/'

parse_and_create(path, path_to_write)

#student
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/student/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/student/strip/'

parse_and_create(path, path_to_write)
