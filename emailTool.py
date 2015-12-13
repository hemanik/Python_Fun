#!/usr/bin/env python

import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('user', help='enter a valid user name')
parser.add_argument('--user',action="store_true",help='username')
parser.add_argument('--email',action="store_true",help='display email')
args = parser.parse_args()

r = requests.get('https://api.github.com/users/' + args.user)
data = json.loads(r.text)

print data['login']

try:
   print data['email']
except KeyError:
   print "Email not provided!!"
