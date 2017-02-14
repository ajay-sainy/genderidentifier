import os
from urllib.request import urlopen
import csv
import pickle
        
def getNameList():
    if not os.path.exists('names.pickle'):
        print ('names.pickle does not exist, generating')
        if not os.path.exists('names.zip'):
            print ('names.zip does not exist, downloading from github')
            #downloadNames()
        else:
            print ('names.zip exists, not downloading')
    
        print ('Extracting names from names.zip')
        namesDict=extractNamesDict()
        print(namesDict)
        maleNames=list()
        femaleNames=list()
        
        print ('Sorting Names')
        for name in namesDict:
            counts=namesDict[name]
            tuple=(name,counts[0],counts[1])
            if counts[0]>counts[1]:
                maleNames.append(tuple)
            elif counts[1]>counts[0]:
                femaleNames.append(tuple)
        
        names=(maleNames,femaleNames)
        
        print ('Saving names.pickle')
        fw=open('names.pickle','wb')
        pickle.dump(names,fw,-1)
        fw.close()
        print ('Saved names.pickle')
    else:
        print ('names.pickle exists, loading data')
        f=open('names.pickle','rb')
        names=pickle.load(f)
        print ('names.pickle loaded')
        
    print ('{} male names loaded, {} female names loaded'.format(len(names[0]),len(names[1])))
    
    return names
    
def downloadNames():
    u = urllib2.urlopen('https://github.com/downloads/sholiday/genderPredictor/names.zip')
    localFile = open('names.zip', 'w')
    localFile.write(u.read())
    localFile.close()
    
def extractNamesDict():
    #zf=ZipFile('names.zip', 'r')
    #filenames=zf.namelist()
    path = r"C:\Users\759946\Downloads\names"
    filenames = os.listdir(path)
    
    names=dict()
    genderMap={'M':0,'F':1}
    
    for filename in filenames:
        print(filename+"asd")
        fpath = str(path+"\\"+filename)
        print(fpath)
        file=open(fpath,'r')
        rows=csv.reader(file, delimiter=',')
        
        for row in rows:
            name=row[0].upper()
            gender=genderMap[row[1]]
            count=int(row[2])
            
            if not name in names:
                names[name]=[0,0]
            names[name][gender]=names[name][gender]+count
            
        file.close()
        print ('\tImported %s',filename)
    return names
if __name__ == "__main__":
    getNameList()