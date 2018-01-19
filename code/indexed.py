import os
from collections import Counter

def indexed(path, fileUser, filewords, train_test):
	i = 0
	for filename in os.listdir(path):
		if "http" in filename:
			'''if train_test == 1:
				print(filename)'''
			with open(path + filename) as f:
				lines = f.readlines()
				counter_words = Counter(lines)
				prev_word = ""
				for words in lines:
					if prev_word != words.rstrip():
						prev_word = words.rstrip()
						clas = path.replace('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train','')
						clas = clas.replace('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test','')
						clas = (clas.replace('porter/','')).replace('/','')
						fileUser.write(words.rstrip()+","+clas+","+filename+","+str(counter_words[words])+"\n")
						filewords.write(words.rstrip()+"\n")

fileUser = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/index.txt', "w+")
filewords = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/words.txt', "w+")

path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/course/porter/'

indexed(path,fileUser,filewords,1)

path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/faculty/porter/'

indexed(path,fileUser,filewords,1)

path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/student/porter/'

indexed(path,fileUser,filewords,1)

fileUser.close()
filewords.close()

index_file = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/index.txt','r')
output = open("/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/sorted_index.txt", 'w')
lines = index_file.readlines()
for line in sorted(lines, key=lambda line: line.split()[0]):
    output.write(line)
output.close()
index_file.close()

index_file = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/words.txt','r')
output = open("/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/sorted_words.txt", 'w')
lines = index_file.readlines()
for line in sorted(lines, key=lambda line: line.split()[0]):
    output.write(line)
output.close()
index_file.close()

os.remove('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/index.txt')
os.remove('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/words.txt')


fileUser = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/index.txt', "w+")
filewords = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/words.txt', "w+")

path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/course/porter/'

indexed(path,fileUser,filewords,0)

path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/faculty/porter/'

indexed(path,fileUser,filewords,0)

path = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/student/porter/'

indexed(path,fileUser,filewords,0)

fileUser.close()
filewords.close()

index_file = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/index.txt','r')
output = open("/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/sorted_index.txt", 'w')
lines = index_file.readlines()
for line in sorted(lines, key=lambda line: line.split()[0]):
    output.write(line)
output.close()
index_file.close()

index_file = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/words.txt','r')
output = open("/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/sorted_words.txt", 'w')
lines = index_file.readlines()
for line in sorted(lines, key=lambda line: line.split()[0]):
    output.write(line)
output.close()
index_file.close()

os.remove('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/index.txt')
os.remove('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/words.txt')