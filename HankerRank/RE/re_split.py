import re


s = "100,000,000.000"
print(*re.split(r'[.,]+', s.strip('., ')),sep='\n')