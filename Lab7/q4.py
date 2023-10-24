import re
f = open('mail.txt','r')
fv = open('valid_mail.txt','w')
fi = open('invalid_mail.txt','w')
pattern = r"^[a-zA-Z][a-zA-Z._1-9]*@[a-zA-Z]*\.[a-zA-Z.]*[(?:com|edu|in)]{3}$"
for mail in f.readlines():
    if re.match(pattern,mail):
        fv.write(mail)
    else:
        fi.write(mail)
f.close()
fv.close()
fi.close()