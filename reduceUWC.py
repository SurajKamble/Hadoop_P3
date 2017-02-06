#!/usr/bin/env python

import sys

unique_word_count = 0
old_year = None
year = []
u_w_c = []

for line in sys.stdin:
    (key, val) = line.strip().split('\t', 1)
    if old_year != key:
        if old_year:
            print '%s\t%s' % (old_year, unique_word_count)
            year.append(old_year)
            u_w_c.append(unique_word_count)
            unique_word_count = 0

    old_year = key
    # year.append(old_year)
    try:
        unique_word_count += int(val)
        # u_w_c.append(unique_word_count)
    except:
        continue

year.append(old_year)
u_w_c.append(unique_word_count)

print '%s\t%s' % (old_year, unique_word_count)

import matplotlib.pyplot as p

p.plot(year, u_w_c, 'o')
# p.yscale('linear')
# p.xscale('linear')
p.show()


'''

#!/usr/bin/env python

import sys
import string

unique_word_count = 0
old_year = None
year = []
u_w_c = []

for line in sys.stdin:
    (key, val) = line.strip().split('\t', 1)
    # print type(key), type(val), type(old_year)
    # print key, val
    if int(val) == 1:
        # print 'in if'
        if old_year != key:
            # print 'in if'
            if old_year:
                # print 'in if'
                print '%s\t%s' % (old_year, unique_word_count)
                year.append(old_year)
                u_w_c.append(unique_word_count)
                unique_word_count = 0
        # print key, 'key'
        old_year = key
        # print old_year, 'old year'
        try:
            unique_word_count += int(val)
        except:
            continue
print '%s\t%s' % (old_year, unique_word_count)

import matplotlib.pyplot as p

p.plot(year, u_w_c)
p.show()

'''
