#!/bin/sh

# A Bourne shell script that converts a text file into a list of words.
# A word is a string of alphabetic letters. Any non-alphabetic characters 
# are considered as word separators. Note that extracted words may not
# be meaningful in English. The extracted words are further converted to 
# lower cases and sorted in alphabetic order.
# Usage: extractwords.sh inputFileName > outputFilename
  
# Check usage
if [ $# -lt 1 ]
then
  echo "Usage: $0 <input text file>" 1>&2
  exit 1
fi

# Check the existence of the input file
if [ ! -f $1 ]
then
  echo "File $1 does not exist" 1>&2
  exit 1
fi

cat $1 |
tr -sc A-Za-z '\012' | # convert file into one word per line
sed -e '/^$/d' |       # delete empty lines (the first line may be empty)
tr 'A-Z' 'a-z' |       # convert upper cases into lower cases
sort                   # sort the words

