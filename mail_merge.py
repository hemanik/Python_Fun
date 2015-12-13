#!/usr/bin/env python

import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('nameList', help="input recepient list")
parser.add_argument('mailText', help="input mail content")
args = parser.parse_args()

dir = os.path.dirname(args.nameList)
with open(args.nameList,'r') as f:

  for name in f:
    temp = os.path.join(dir, name+'.txt')

    with open(temp,'a')as outfile:
       outfile.write(name)

       fb = open(args.mailText,'r')
       content = fb.read()
       outfile.write(content)
       fb.close()

