# pattern matching
# re-- package for pattern matching

import re
c=0
# finditer for iteration and check
# ethan search ethil annu
matcher =re.finditer('ab','abaaabbab')
for match in matcher:
    c+=1
print('count:',c)