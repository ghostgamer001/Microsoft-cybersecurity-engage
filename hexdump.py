#hexdump for malicious file
import binascii

hexfile = open("c:/Users/KIIT/AppData/Local/Temp/Temp1_hexdump-3.3.zip/hex.txt", "a")

with open('c:/Users/KIIT/AppData/Local/Temp/Temp1_hexdump-3.3.zip/hello.exe', 'rb') as f:
    chunks = iter(lambda: f.read(32), b'')
    hexlines = map(binascii.hexlify, chunks)
    for hexline in hexlines:
        hexfile.write(hexline.decode() + "\n")
    
    f.close()

#store hexdump of malicious function in list f    
f=['hex1','hex2','hex3','hex4','hex5','hex6','hex7','hex8','hex9','hex10']

c=0
# mylines = []                               
with open ('file.txt', 'rt') as myfile:
    mylines = myfile.readlines()    
    # for myline in myfile.readlines():                   
    #     mylines.append(myline.rstrip('\n')) 

for line in mylines:
    line = line.rstrip('\n')
    for str in f:
        if str is line:
            c+=1
if c>=5:
   print("File possess botnet capabilities")
else:
   print("File fail botnet capabilities")