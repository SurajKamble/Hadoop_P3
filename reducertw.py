#!/usr/bin/env python

import sys
import string

Santa_count = 0
other_count = 0
Santa_wc=0
other_wc=0
avg_Santa=0
avg_others=0

for line in sys.stdin:
  (key,val) = line.split('\t',1)

  if key=='count_Santa':
    Santa_count=Santa_count + int(val)
  elif key=='count_other':
    other_count=other_count + int(val)
  elif key=='wc_Santa':
    Santa_wc=Santa_wc + int(val)
  elif key=='wc_other':
    other_wc=other_wc + int(val)
avg_Santa=Santa_wc/Santa_count
avg_others=other_wc/other_count
print '%s\t%s' % ('Santa_tweetavg',avg_Santa)
print '%s\t%s' % ('other_tweetavg',avg_others)
