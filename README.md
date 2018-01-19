# Web Page Classifier

The goal is to perform a classification of Web pages. I have available a training data set containing a collection of Web pages from two computer science departments, and a test data set containing a collection of Web pages from another computer science department. The pages in these two data sets are hand-classified into the following categories:

Student
Faculty
Course

The goal is to be able to learn a Web page classifier from the training data, and then use the classifier to classify the Web pages in the test data set.

## Steps for preprocessing the data

### 1. Remove MIME-header from all files and strip the files from HTML tags

For this step I used a python script called strip.py. Every file had a MIME-header, which contained mostly the same words for each file, making the words on the header useless. I decided to delete the Mime-header in order to get a more accurate classification.

First strip.py would read each file and delete all the lines at the beginning of the file that belonged to the MIME-header. Then, once I have striped the header, the second step was to strip the web files from their HTML tags since they are not useful to classify web pages. I added to strip.py the Python library BeautifulSoup to extract the text from HTML tags.

### 2. Extract the words from the files given by step 2

Now that I have only plain text from the HTML files, I needed to extract each word from the output provided in step 1. I ran a script I downloaded (extractmultfiles.sh). The script would output the list of words that appear in each file.	

### 3. Remove Stop Words

This step removes stop words from the extracted words. To carry out this task, I wrote a python script stop_words.py.

### 4. Stemming

This step replaces each words in each file with their stems if necessary. I used the Porter stemming algorithm (porter.py) to perform the stemming on the files provided by step 3. I had to make minor modifications to the algorithm to make it write the words on the text files I wanted.

### 5. Build an inverted index file for the training data set

I constructed an inverted text file for all words in the training data and another one for all the words in the testing data, the index was structured as follows:

The first column is the word, the second column is the directory/class, the third column is the name of the files where the word appears, and last column is the number of times the word appears in the file. 

If a word appears in multiple web pages, it will appear multiple times in the text file.
The lines are sorted by the alphabetic order of the words. I wrote a python script: indexed.py which gives the sorted index file from the files given by step 4. Here is an extract of the output file:

aaai,faculty,http:^^www.cs.utexas.edu^users^porter^.words,2
aaai,faculty,http:^^www.cs.washington.edu^homes^etzioni^.words,2
aaai,faculty,http:^^www.cs.washington.edu^homes^weld^weld.html.words,3
aaai,student,http:^^www.cs.washington.edu^homes^dbc1^.words,1
aait,faculty,http:^^www.cs.utexas.edu^users^porter^.words,1
aaj,student,http:^^www.cs.utexas.edu^users^gooty^.words,1
aavail,course,http:^^www.cs.washington.edu^education^courses^531^CurrentQtr^.words,1
abbott,course,http:^^www.cs.utexas.edu^users^vin^cs384m.html.words,1
abbrevi,faculty,http:^^www.cs.washington.edu^people^faculty^lazowska^.words,1
abc,student,http:^^www.cs.utexas.edu^users^ulf^.words,1
abduct,faculty,http:^^www.cs.washington.edu^homes^bershad^.words,1
abel,course,http:^^www.cs.washington.edu^education^courses^467^Fall96^.words,1
aberman,course,http:^^www.cs.washington.edu^education^courses^421^.words,1

### 6. Calculate tf-idf for the training data set

In order to select a « bag of words » with the Information Gain attribute selection algorithm from WEKA, I have to generate a CSV file. The columns are all the words from the training data set and the rows are the 466 different files. The CSV file should look like this: 

To generate this CSV file, I wrote the python script: tf-idf.py which calculates the tf-idf for each word of each page of the training data set. 

The output (tf-idf.txt) looks like this:
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,addit,4.96981329958
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,consult,4.18965474203
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,contact,1.38629436112
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,cours,3.295836866
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,cs,0.0
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,edu,0.0
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,faculti,2.48490664979
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,fall,1.79175946923
http:^^www.cs.utexas.edu^users^UTCS^courses^.words,course,gloria,6.14418563413

The first column is the file name, the second one is the class, the third one is the words from the page and the last one is the tf-idf. The file is sorted by files name in order to make the insertion of values in the cvs file easier.

Then, the script convert_csv.py will go over the output provided by tf-idf.py (projectdata/train/sorted_tfidf.txt) and build the CSV file (as shown in figure 2).

### 7. Use Information Gain to select the bag of words

Once I have the training data table, I needed to determine which bag of words to select. I used WEKA and the Information Gain feature it provides. 

First I had to upload the file to WEKA. Then, I deleted the column « Name » (ID type column) which is irrelevant for classification. Then, I saved the file as an .artff. 

Finally, I ran Information Gain by using the Filter feature in the Preprocess tab and chose: supervised->attribute->AttributeSelection.

For the Ranker method, I first chose a threshold of 0 which means that every word which has an Information Gain > 0 is selected.

450 words were given by WEKA which is my « bag of words ».
I saved the file in arff format after applying the filter. The file train_data.arff (in the project directoy) is the training data table based on the selected words.

### 8. Build the test data table based on the selected word

To do this step, I programmed this script: convert_test_csv.py. 
This script calculates the tf-idf of the selected words for every file from the test training set. The output is a CSV file which is as following:

I uploaded the file to WEKA. I deleted the column «Name» and I converted it in arff format. I had to modify the following line in the arff file: @attribute Class {course, student, faculty} to make it match exactly the line from the arff file of the training data table.

The data preprocessing is now done and I have our training data table and test data table. These files are given in the repository:
train_data.arff
test_data.arff

## II. Learning algorithms in WEKA

To choose the best learning algorithm in WEKA, I ran cross-validation with 10 folds on the training set. I tested all the possible algorithms and I chose the algorithms which gave the biggest number for « Correctly Classified Instance ». 
Two algorithms had the exact same percentage of correctly classified instance: trees.LMT and functions. SimpleLogistics and trees. LMT gave 90.7725% of correctly classified instances.So I used LMT totest the accuracy of our learnt models on the test data.
 
## III. Testing statistics of the learned models on the test data

I tested the LMT algorithm on the test set. The confusion matrix and the accuracy are the same for the 2 algorithms. I had an accuracy of 91.7476% on the test data set.
