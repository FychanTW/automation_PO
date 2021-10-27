from PyQt5 import QtWidgets
import os,fnmatch
import pdf2txt as p2t

#initial check1: create necessary folder if not found
#initial check2: move unprocessed files to backup folder and create log 
def initial_check(arg):
    tmp_dir = os.getcwd()

#loadPO: check files in the unprocessed PO folder, ftype=.pdf
#loadPO: display the file names in the Qt PO_listView
#loadPO: call covert PO
def loadPO(arg):
    tmp_dir = os.getcwd()
    dirname = QtWidgets.QFileDialog.getExistingDirectory(arg,'Select PO folder:',tmp_dir)
    listofFiles = os.listdir(dirname)
    #print(listofFiles)
    arg.model.setStringList(listofFiles)
    arg.PO_listView.setModel(arg.model)
    arg.CurrentDirLabel.setText(repr(dirname))
    convertPO(arg,listofFiles,dirname)

#loadToken: load Trello API keys and token
def loadToken(arg):
    tmp_dir = os.getcwd()
    fname = QtWidgets.QFileDialog.getOpenFileName(arg,'Open file',tmp_dir)
    f = open(fname[0],'r',encoding='UTF-8')
    Token_data = f.read().split('\n')
    f.close()
    return Token_data

#convertPO: convert the existed PO pdf files into text file by pdf2text module
#extractPO: call extractPO
def convertPO(arg,listOfFiles,dirname):
    pattern = "ZK*.pdf"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            #print(entry)
            tmp_name = entry[0:-4]+'.txt'
            #print(tmp_name)
            p2t.main(['-o'+'.\\extracted_text\\'+tmp_name,'.\\sample_PO\\' + entry])
            extractPO(arg,tmp_name)
        #os.rename('.\\'+entry,'..\\archive_PO\\'+'done_'+entry)

#extractPO: extract the PO number from the text file
#extractPO: display the PO number on Qt PONum_listView
def extractPO(arg,textfilename):
    tmp_dir = os.getcwd()
    os.chdir('.\\extracted_text')
    f = open(textfilename,'r',encoding='UTF-8')
    fdatalines = f.readlines()
    tmp_list = arg.PONum_model.stringList()
    for data in fdatalines:
        if data[0:4]=='発注番号':
            #print('the PO number is:',data[-12:-1])
            PO_Number = data[-12:-1]
            tmp_list.append(PO_Number)
            arg.PONum_model.setStringList(tmp_list)
            break
    f.close()
    os.chdir(tmp_dir)
    arg.PONum_listView.setModel(arg.PONum_model)

def pushTrello(arg):
    print("")