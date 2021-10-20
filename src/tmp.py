from typing import Pattern
import pdf2txt as p2t
#p2t.main(['-o extract1.txt','..\\sample_PO\\test1.pdf'])
import os, fnmatch
current_dir = os.getcwd()
print("Current Directory is: ",current_dir)
#file_to_open  = os.path.join(current_dir,"test1.pdf")
#f = open('..\\sample_PO\\test1.pdf')
#f.close()
listOfFiles = os.listdir('.\\sample_PO')
os.chdir('.\sample_PO')
print(os.getcwd())
pattern = "ZK*.pdf"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        print(entry)
        os.rename('.\\'+entry,'..\\archive_PO\\'+'done_'+entry)
