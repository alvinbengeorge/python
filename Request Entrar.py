import requests
import cloudscraper
header={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','referer':"https://entrar.in"}
aheader={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
suvzsjv={
    'username': 'username',
    'password': 'password',
    'captcha':'0'
    }
announcement_data={
    'announcementlist': 'true',
    'session': '205'
    }
with requests.Session() as s:
    scraper=cloudscraper.create_scraper(sess=s)
    r=scraper.get("https://entrar.in/login/login",headers=aheader)
    st=r.content.decode()
    print(st)
    start_captcha=st.find('<span class="label-input100" style="font-size: 18px;">')+len('<span class="label-input100" style="font-size: 20px;">')
    end_captcha=st.find("=",start_captcha)
    print(st[start_captcha:end_captcha])
    print(str(eval(st[start_captcha:end_captcha])))
    suvzsjv['captcha']=str(eval(st[start_captcha:end_captcha]))
    print(suvzsjv)
    url="https://entrar.in/login/auth/"
    r=scraper.post(url,data=suvzsjv,headers=aheader)
    r=scraper.get("https://entrar.in/",headers=header)
    print("1st")
    print(r.content.decode())
    r=scraper.post("https://entrar.in/parent_portal/announcement",headers=header)
    r=scraper.get("https://entrar.in/parent_portal/announcement",headers=header)
    r=scraper.post("https://entrar.in/parent_portal/announcement",data=announcement_data,headers=header)
    st=r.content.decode()
    print(st)
    for i in range(1,4):
        try:
            a=st.find('<td class="text-wrap">'+str(i)+'</td>')
            b=st.find('<td class="text-wrap">'+str(i+1)+'</td>')
            print(a)
            le=len('<td class="text-wrap">'+str(i+1)+'</td>')-1
            if b==-1:
                print("End of List")
                break
            c=st.find('&nbsp;&nbsp; ',a,b)+len("&nbsp;&nbsp; ")
            d=st.find('<',c,b)
            out=st[c:d].strip()
            e=a+le
            f=st.find('<td>',e,e+15)+len('<td>')
            g=st.find('</td>',e,e+45)
            date=st[f:g]
            h=st.find('<a target="_blank" href="',a,b)+len('<a target="_blank" href="')
            j=st.find('"',h+3,b)
            link=str(st[h:j])
            req=scraper.get(link)
            print(req.headers['date'])
            print(out,":",date,":",link)
            with open((str(i)+".pdf"),'wb') as pdf:
                pdf.write(req.content)
            print("Downloaded")
        except Exception as e:
            print(e)
        
