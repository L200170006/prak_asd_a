#Bagus Nuril Anam L200170006
#Nomor 1
import re
f=open('Indonesia.txt','r', encoding='latin1')
teks = f.read()
f.close()
p=r'me\w+'
string = re.findall(p,teks)
print(string)
