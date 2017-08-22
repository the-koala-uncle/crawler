import psutil,os, configparser
def kill(path):
    pidList = psutil.pids()

    for pid in pidList:
        pidDictionary = psutil.Process(pid).as_dict(attrs=['name']);
        for keys in pidDictionary.keys():
            try:
                config.get('system',str(pidDictionary['name']))
            except:
                try:
                    psutil.Process(int(pid)).terminate()
                except:
                    print(str(pidDictionary['name'])+'没有被结束')


    print('-------end-------')
