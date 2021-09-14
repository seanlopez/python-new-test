import re

line = "sjulia@gmail.com"
print(re.search("(?<=\@)(.*)(?=\.com)",line).group())
