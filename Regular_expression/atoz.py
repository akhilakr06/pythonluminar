import re
x="[a-z]"
matcher=re.finditer(x,"abt9 c@5kzAz")
for match in matcher:
    print(match.start())
    print(match.group())