import urllib.request
import requests
import time
import cloudscraper
from datetime import date
content1={'filter':'true','from':str(date.today())}
print(date.today())
header={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','referer':"https://entrar.in"}
header1={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','referer':"https://entrar.in/classroom_creation_crm_new/s_display"}
content={'username':"username",'password':"password",'captcha':'0'}
url_dup=""
with requests.Session() as s:
    scraper=cloudscraper.create_scraper(sess=s)
    st=""
    url="https://entrar.in/login/auth/"
    r=scraper.get("https://entrar.in/login/login",headers=header)
    st=r.content.decode()
    start_captcha=st.find('<span class="label-input100" style="font-size: 18px;">')+len('<span class="label-input100" style="font-size: 20px;">')
    end_captcha=st.find(" = </span>",start_captcha)
    content['captcha']=str(eval(st[start_captcha:end_captcha]))
    print(content['captcha'])
    r=scraper.post(url,data=content,headers=header)
    print(r.content.decode())
    r=scraper.get("https://entrar.in/",headers=header)
    print(r.content.decode())    
    rout=scraper.post("https://entrar.in/classroom_creation_crm_new/s_display",data=content1,headers=header1)    
    #Data Not Found.
    print(rout.content.decode())
    while str(rout.content.decode()).find(">Join<")==-1:        
        rout=scraper.post("https://entrar.in/classroom_creation_crm_new/s_display",data=content1,headers=header1)
        print("Class not found")
        time.sleep(1)
    print("Class available")
    st=rout.content.decode()
    #print(st)
    check_1=st.find('<a href="')+len('<a href="')
    check_2=st.find('"',check_1+2)
    print(check_1,check_2)
    url=st[check_1:check_2]
    r=s.get(url,headers=header)
    url_dup=url
    print(url)
    r=scraper.get(url_dup,headers=header1)
    st=r.content.decode()
    start_st=st.find('window.location.assign("')+len('window.location.assign("')
    end_st=st.find('");',start_st)
    url=st[start_st:end_st]
    r=scraper.get(url,headers=header1)
    st=r.content.decode()
    temp=st.find("entrarlive.")
    host=st[st.find("live",temp-10):temp+len("entrarlive.co")]
    temp=st.find('<script type="text/javascript" src="')+len('<script type="text/javascript" src="')
    js=st[temp:st.find('">',temp)]
    print(js)
    print(host)
    r=scraper.get("https://"+host+js,headers=header1)
    st=r.content.decode()
    sto=0
    for i in range(0,100):
        num=st.find("session",sto)
        print(st[num-100:num+100])
        sto=num+1
    
