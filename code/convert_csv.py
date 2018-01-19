import csv
import copy
import io
from collections import Counter

def populate_empty_cells(words):
	new_dict = {}
	wordlist = open(words, "r+")
	lines = wordlist.readlines()
	counter_words = Counter(lines)
	new_dict.keys()
	for key in sorted(counter_words.keys()):
		key = key.replace("\n","")
		new_dict[key] = 0
	return new_dict



def create_data_table(list_words,index,csv_file):
	wordlist = open(list_words, "r+")
	lines = wordlist.readlines()

	fieldnames = ['Name']
	counter_words = Counter(lines)
	for key in sorted(counter_words.keys()):
		key = key.replace("\n","")
		fieldnames.append(key)
	fieldnames.append('Class')
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()

	sorted_index = open(index, "r+")
	lines = sorted_index.readlines()
	prev_doc = ""
	i=0
	dicto = populate_empty_cells(list_words)
	for words in lines:
		doc, clas, word, tfidf = words.rstrip().split(',')
		if prev_doc != doc and i==0:
			i += 1
			new_dict = copy.deepcopy(dicto)
			new_dict["Name"] = doc
			if word in dicto:
				new_dict[word] = tfidf
				new_dict["Class"] = clas
			prev_doc = doc
		elif prev_doc != doc:
			writer.writerow(new_dict)
			new_dict = copy.deepcopy(dicto)
			new_dict["Name"] = doc
			if word in dicto:
				new_dict[word] = tfidf
				new_dict["Class"] = clas
			prev_doc = doc
		else:
			if word in dicto:
				new_dict[word] = tfidf
				new_dict["Class"] = clas
	writer.writerow(new_dict)

words = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/sorted_words.txt'
index = '/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/sorted_tfidf.txt'
csv_file = open('/Users/jazpurc/Documents/YorkU/EECS4412/projet/projectdata/train/train_data.csv', 'w', newline='')
create_data_table(words,index,csv_file)
csv_file.close()