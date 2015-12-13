#!/usr/bin/env python

import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='enter a valid file name')
parser.add_argument('-l', "--line",action="store_true", help='number of lines(default: find no of words)')
args = parser.parse_args() 

#fname = "feed.txt"

num_lines = 0
num_words = 0

if os.path.exists(args.filename):

	with open(args.filename,'r') as f:
  		 for line in f:
       			 words = line.split()

        		 num_lines += 1 
              		 num_words += len(words)
       		         
#print 'Number of Lines:' 
if args.line:
   print  num_lines
#print 'Number of Words:'
else:
   print  num_words
     

