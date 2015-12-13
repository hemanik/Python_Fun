#!/usr/bin/env python

for i in xrange(1,101):
  if i%3 == 0:
    if i%5 == 0:
       print 'FizzBuzz'
    print 'Fizz'
  elif i%5 == 0:
     print 'Buzz'
  else:
     print i


 
 
   
