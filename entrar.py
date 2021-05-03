import urllib.request
import requests
import time
from datetime import date
content1={'filter':'true','from':str(date.today())}
print(date.today())
header={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','referer':"https://entrar.in"}
header1={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','referer':"https://entrar.in/classroom_creation_crm_new/s_display"}
content={'username':"username",'password':"password"}
with requests.Session() as s:
    st=""
    url="https://entrar.in/login/authenticate1/"
    r=s.post(url,data=content,headers=header)
    r=s.get("https://entrar.in/",headers=header)
    print(r.content.decode())    
    rout=s.post("https://entrar.in/classroom_creation_crm_new/s_display",data=content1,headers=header1)    
    #Data Not Found.
    print(rout.content.decode())
    while str(rout.content.decode()).find(">Join<")==-1:        
        rout=s.post("https://entrar.in/classroom_creation_crm_new/s_display",data=content1,headers=header1)
        print("Class not found")
        time.sleep(1)
    print("Class available")
    st=rout.content.decode()
    #print(st)
    check_1=st.find('<a href="')+len('<a href="')
    check_2=st.find('"',check_1+2)
    print(check_1,check_2)
    print(st[check_1:check_2])
    url=st[check_1:check_2]
    r=s.get(url,headers=header)
    url_dup=url
    st=r.content.decode()
    print(st)
    check_1=st.find('window.location.assign("')+len('window.location.assign("')
    check_2=st.find('");',check_1+2)
    url=(st[check_1:check_2])
    print(url)
    fullname=st[url.find("fullName="+len("fullName=")):url.find("&",url.find("fullName="+len("fullName=")))]
    ID=st[url.find("meetingID="+len("meetingID=")):url.find("&",url.find("meetingID="+len("meetingID=")))]
    Password=st[url.find("password="+len("password=")):url.find("&",url.find("password="+len("password=")))]
    checksum=st[url.find("checksum="+len("checksum=")):url.find("&",url.find("checksum="+len("checksum=")))]
    content2={
        'fullName':str(fullname),
        'meetingID':str(ID),
        'password':str(Password),
        'redirect':'true',
        'checksum':str(checksum),
        }
    r=s.post(url_dup,data=content2,headers=header)
    print(r.content.decode())
