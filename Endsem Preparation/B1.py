#                           REGEX
# 1) if starting with vowel and ending with consonant, append "ing" to word 
# 2) if it has two special characters, add * to starting of word

import re
s = input('Enter String: ')
if re.match(r"^[AEIOUaeiou]",s):
    s+="ing"  
if re.match(r".*([^A-Za-z0-9]).*([^A-Za-z0-9]).*",s):
    s = "*"+s 
print(s)