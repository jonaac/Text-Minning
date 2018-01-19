import os
from copy import copy


def stop_words(path, path_to_write):

	filenameStopWords = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/stop_words.txt'

	with open(filenameStopWords) as filenameStopWords:
		stopWords = filenameStopWords.readlines()

	for filename in os.listdir(path):
		with open(path + filename) as f:
			lines = f.readlines()
			ouputLines = copy(lines)
			# remove stop words
			for word in lines:
				if word in stopWords:
					ouputLines.remove(word)
			# rewrite file
			fileUser = open(path_to_write + filename, "w+")
			for word in ouputLines:
				fileUser.write(word)
			fileUser.close()
			
#course
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/course/words/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/course/stop/'

stop_words(path, path_to_write)

#faculty
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/faculty/words/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/faculty/stop/'

stop_words(path, path_to_write)

#student
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/student/words/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/student/stop/'

stop_words(path, path_to_write)

# Test set:
#course
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/course/words/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/course/stop/'

stop_words(path, path_to_write)

#faculty
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/faculty/words/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/faculty/stop/'

stop_words(path, path_to_write)

#student
path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/student/words/'
path_to_write = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/student/stop/'

stop_words(path, path_to_write)


