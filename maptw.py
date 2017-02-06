#!/usr/bin/env python

import sys
import string
import json

count_Santa=0
count_other=0
wc_Santa=0
wc_other=0
lc_Santa=0
for line in sys.stdin:
  d=json.loads(line)
  if d['user']['screen_name']=='PrezOno':
    time=d['text']
    lc_Santa=len(time)

      

    wc_Santa=wc_Santa+lc_Santa
    count_Santa=count_Santa+1

  else:
    tw=d['text']

    lc_others=len(tw)


    wc_other=wc_other+lc_others
    count_other=count_other+1
print '%s\t%s' % ('wc_Santa',wc_Santa)
print '%s\t%s' % ('wc_other',wc_other)
print '%s\t%s' % ('count_Santa',count_Santa)
print '%s\t%s' % ('count_other',count_other)  
