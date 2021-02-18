import re

phReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phReg.search('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')

print(mo)