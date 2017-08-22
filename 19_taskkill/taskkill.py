import psutil,os, configparser
os.chdir (os.getcwd ())
def kill(filepath):
    pidList = psutil.pids()
    config = configparser.ConfigParser()
    config.read(filepath)
    for pid in pidList:
        pidDictionary = psutil.Process(pid).as_dict(attrs=['name']);
        for keys in pidDictionary.keys():
            try:
                config.get('task',str(pidDictionary['name']))
            except:
                try:
                    psutil.Process(int(pid)).terminate()
                except:
                    print(str(pidDictionary['name'])+'没有被结束')


    print('-------end-------')
kill('0.ini')
##import psutil,os,time
##  
##outputFile = open('output'+str(time.time())+'.txt','a+')
##  
##pidList = psutil.pids()
##  
##for pid in pidList:
##    pidDictionary = psutil.Process(pid).as_dict(attrs=['pid', 'name', 'username','exe','create_time']);
##    for keys in pidDictionary.keys():
##        tempText = keys + ':' + str(pidDictionary[keys]) + '\n'
##        outputFile.write(tempText)
##    outputFile.write('*********************\n')
##  
##outputFile.close()
