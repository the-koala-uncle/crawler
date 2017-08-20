import requests, json, hashlib, configparser

def md5(word):
    word = word.encode("utf-8")  
    m= hashlib.md5()  
    m.update(word)  
    return m.hexdigest()

def is_alphabet(uchar):
    if (uchar>= u'\u0041'and uchar<=u'\u005a')or(uchar >= u'\u0061'and uchar<=u'\u007a'):
        return(True)
    else:
        return(False)

def translate(q='请输入'):
    config = configparser.ConfigParser()
    config.read(filepath)
    

    
    appid = config.get('fanyi_baidu','ID')
    psw = config.get('fanyi_baidu','密钥')

    if is_alphabet(q):
        fromm= 'en'
        to='zh'
    else:
        fromm= 'zh'
        to='en'
    salt='1435660288'

    sign=md5(appid+q+salt+psw)
    
    url='http://api.fanyi.baidu.com/api/trans/vip/translate?q='+q+'&from='+fromm+'&to='+to+'&appid='+appid+'&salt='+salt +'&sign='+sign
    res=requests.get(url)

    json_dict=json.loads(res.text)
    try:
        print(json_dict["trans_result"][0]["dst"])
    except:
        print(res.text)
translate()
