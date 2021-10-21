from typing import Pattern
import pdf2txt as p2t
import os, fnmatch
#current_dir = os.getcwd()
#print("Current Directory is: ",current_dir)
#file_to_open  = os.path.join(current_dir,"test1.pdf")
#f = open('..\\sample_PO\\test1.pdf')
#f.close()
def extractPO2txt():
    listOfFiles = os.listdir('.\\sample_PO')
    os.chdir('.\\sample_PO')
    print(os.getcwd())
    pattern = "ZK*.pdf"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
            tmp_name = entry[0:-4]+'.txt'
            print(tmp_name)
            p2t.main(['-o'+'..\\extracted_text\\'+tmp_name,'..\\sample_PO\\' + entry])
        os.rename('.\\'+entry,'..\\archive_PO\\'+'done_'+entry)
