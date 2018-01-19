import os
import math
from collections import Counter

def tf_idf(sorted_index,word_list,N):
	i = 0
	sortedindex = open(sorted_index, "r+")
	wordlist = open(word_list, "r+")
	lines = sortedindex.readlines()
	lines_words = wordlist.readlines()
	counter_words = Counter(lines_words)
	for words in lines:
		word, clas, doc, tf = words.rstrip().split(',')
		tfidf = float(tf) * math.log(N/counter_words[word + "\n"])
		tfidfFile.write(doc+","+clas+","+word+","+str(tfidf)+"\n")
	sortedindex.close()
	wordlist.close()

tfidfFile = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/tfidf.txt', "w+")
sorted_index = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/sorted_index.txt'
word_list = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/sorted_words.txt'

tf_idf(sorted_index,word_list,466)
tfidfFile.close()

index_file = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/tfidf.txt','r')
output = open("/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/sorted_tfidf.txt", 'w')
lines = index_file.readlines()
for line in sorted(lines, key=lambda line: line.split()[0]):
    output.write(line)
output.close()
index_file.close()

os.remove('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/tfidf.txt')


tfidfFile = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/tfidf.txt', "w+")
sorted_index = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/sorted_index.txt'
word_list = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/sorted_words.txt'

tf_idf(sorted_index,word_list,207)
tfidfFile.close()

index_file = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/tfidf.txt','r')
output = open("/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/sorted_tfidf.txt", 'w')
lines = index_file.readlines()
for line in sorted(lines, key=lambda line: line.split()[0]):
    output.write(line)
output.close()
index_file.close()

os.remove('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/test/tfidf.txt')