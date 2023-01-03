import requests
import random 
import hashlib


def login(USERNAME,PASSWORD,url="http://192.168.1.1") -> bool:
    """
    Logins in wifi page.
    """
    # needed for pre request
    session = requests.session()

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"en-GB,en",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Content-Length":"186",
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"_TESTCOOKIESUPPORT=1",
        "Host":"192.168.1.1",
        "Origin":"http://192.168.1.1",
        "Referer":"http://192.168.1.1/",
        "Sec-GPC":"1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    true_pass = PASSWORD
    UserRandomNum = round(random.random()*89999999)+10000000
    Password = hashlib.sha256(bytes(true_pass + str(UserRandomNum),encoding="utf-8")).hexdigest()
    # get checktoken from pre request
    Frm_Loginchecktoken  = str(session.get("http://192.168.1.1").text).split('Frm_Loginchecktoken", "')[-1].split('");')[0]

    data = {
        "Username":USERNAME,
        "action":"login",
        "Password":Password,
        "Frm_Logintoken":0,
        "UserRandomNum":UserRandomNum,
        "Frm_Loginchecktoken":Frm_Loginchecktoken
    }
    # I don'nt think so if there is any other error
    errors = ["You have login failed for three times","User information is error, please input again"]
    request = session.post("http://192.168.1.1",data=data,headers=headers).text
    for error in errors:
        if error in request:
            return False
    return True


USERNAME = "admin"
PASSWORD = "testpass"

print(login(USERNAME,PASSWORD))
