#!/usr/bin/python

#import argparse
import requests
import json

r = requests.get('https://api.github.com/repos/hemanik/test1/commits') 
commit_list = json.loads(r.text)

for d in commit_list:
  print d['sha'] 

