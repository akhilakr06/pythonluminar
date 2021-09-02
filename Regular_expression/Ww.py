import re
x="\W"#\w
matcher=re.finditer(x,"abtA c@5kzAz")
for match in matcher:
    print(match.start())
    print(match.group())